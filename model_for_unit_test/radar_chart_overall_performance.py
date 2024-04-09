import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
labels=np.array(['Technical Proficiency', 'Preparation', 'Cultural Fit', 'Attitude', 'Communication', 'Adaptability'])
stats=np.array([80, 70, 90, 75, 85, 80])

# Number of variables
num_vars = len(labels)

# Compute angle each bar is centered on:
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# Repeat the first value to close the circle
stats=np.concatenate((stats,[stats[0]]))
angles+=angles[:1]

# Plot
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
ax.fill(angles, stats, color='blue', alpha=0.25)
ax.plot(angles, stats, color='blue', linewidth=2)  # Change the color if desired

# Labels for each point
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)

# Title
ax.set_title('Interviewee Performance Radar Chart', y=1.1)

# Show the plot
plt.show()
