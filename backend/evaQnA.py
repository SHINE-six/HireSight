import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import pyreft


# Set device
device = "cuda" if torch.cuda.is_available() else "cpu"

# Load the base model
model_name_or_path = "microsoft/Phi-3-mini-4k-instruct"
model = AutoModelForCausalLM.from_pretrained(
    model_name_or_path, torch_dtype=torch.bfloat16, trust_remote_code=True, device_map=device)

# Load the fine-tuned model using PyReFT
reft_model = pyreft.ReftModel.load(
    "HireSight\\backend\\model\\evaQnAModel", model
)

reft_model.set_device("cuda")

prompt_no_input_template = """\n<|user|>:%s</s>\n<|assistant|>:"""


def main(instruction):
    # Input instruction

    # Tokenize and prepare the input
    tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)
    prompt = prompt_no_input_template % instruction
    inputs = tokenizer(prompt, return_tensors="pt").to(device)

    # Define the base position (last position of the input)
    base_unit_location = inputs["input_ids"].shape[-1] - 1  # last position

    # Generate the output using the fine-tuned model
    _, reft_response = reft_model.generate(
        base={"input_ids": inputs["input_ids"]},  # Pass input as a keyword argument
        unit_locations={"sources->base": (None, [[[base_unit_location]]])},
        intervene_on_prompt=True, max_new_tokens=512, do_sample=True,
        eos_token_id=tokenizer.eos_token_id
    )

    # Decode and print the output
    output_text = tokenizer.decode(reft_response[0], skip_special_tokens=True)
    result = output_text.split(':')[-1].strip()
    return result

print(main("What is the capital of France?"))


