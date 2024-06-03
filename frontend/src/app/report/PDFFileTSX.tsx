'use client'
import {Page, Text, View, Document, StyleSheet, render, PDFViewer, Font, Image} from '@react-pdf/renderer';
import { get } from 'http';
import { get } from 'http';
import * as React from 'react';
import { useState, useEffect } from "react";
// import info from '../../../public/assets/ReportInfo.json'

const styles = StyleSheet.create({
    page:{
        backgroundColor: 'white',
        paddingLeft: 60,
        paddingRight: 60,
        paddingTop: 60,
        paddingBottom: 60,
    },
    body: {
        display: 'flex',
        flexDirection: 'column',
    },
    reportTitle: {
        textDecoration: 'underline',
        textAlign: 'center',
        fontSize: 20,       
        fontFamily: 'Times-Bold', 
        marginBottom: 10, // Adjust as needed
    },
    reportSubTitle: {
        textDecoration: 'underline',
        textAlign: 'left',
        fontSize: 16,
        fontFamily: 'Times-Bold', 
        paddingTop: 10, // Adjust as needed
    },
    reportText: {
        fontSize: 12,
        fontFamily: 'Times-Roman', 
        textAlign: 'justify',
        paddingTop: 5, // Adjust as needed
    },
    reportSupTextBold: {
        fontSize: 14,
        fontFamily: 'Times-Bold', 
        paddingTop: 5, // Adjust as needed  
    },
    reportTextBold: {
        fontSize: 12,
        fontFamily: 'Times-Bold', 
    },
    charts: {
        height: '200px',
        width: '300px',
    },
    pageNumbers: {
        position: 'absolute',
        bottom: 30,
        left: 0,
        right: 0,
        textAlign: 'center',
        fontSize: 12,
        color: 'grey',
    },
    seperateLineDesign: {
        fontSize: 12,
        fontFamily: 'Times-Roman', 
        textAlign: 'justify',
        paddingTop: 5, // Adjust as needed
        paddingBottom: 5, // Adjust as needed
    },
});

const SubTitle =({text}: {text: string}) => (
    <View style={styles.reportSubTitle}>
        <Text>{text}</Text>
    </View>
);

const NormalText = ({text}: {text: string}) => (
    <View style={styles.reportText}>
        <Text>{text}</Text>
    </View>
);

const BoldText = ({text}: {text: string}) => (
    <View style={styles.reportTextBold}>
        <Text>{text}</Text>
    </View>
);

const SupBoldText = ({text}: {text: string}) => (
    <View style={styles.reportSupTextBold}>
        <Text>{text}</Text>
    </View>
);

const BulletNormalText = ({text}: {text: string}) => (
    <View style={styles.reportText}>
        <Text>{'\u2022  '} {text}</Text>
    </View>
);

const BlankLine = () => (
    <View style={styles.reportText}>
        <Text>{'\n'} </Text>
    </View>
);

const SeperateLine = () => (
    <View style={styles.seperateLineDesign}>
        <Text>{"__________________________________________________________________________"} </Text>
    </View>
);

interface information{
    "_id": {
        "$oid": string
      },
      "UniqueSessionID": string,
      "InterveweeName": string,
      "InterveweeID": string,
      "InterviewPosition": string,
      "overallSuitability": null,
      "InterviewDate": string,
      "RadarChartBinaryArray": string,
      "RadarChartSummary": null,
      "MBTIBinaryArray": string,
      "aiReport": {
        "RadarChartSummary": string,
        "TechnicalSkill": {
          "TechnicalSkillScore": number,
          "TechnicalSkillSummary": string
        },
        "SoftSkill": {
          "PreparationSkill": {
            "PreparationScore": number,
            "PreparationDetailScoring": {
              "Knowledge of the Company, Role, and Industry": number,
              "Quality of Questions for the Interviewer": number,
              "Alignment of Skills and Experiences with Job Requirements": number,
              "Formal and Appropriate Attire": number,
              "Grooming and Tidiness": number
            },
            "PreparationSummary": string
          },
          "CulturalFitSkill": {
            "CulturalFitScore": number,
            "CulturalFitDetailScoring": {
              "Alignment with Core Company Values": number,
              "Professionalism and Work Ethic": number,
              "Teamwork and Collaboration Style": number,
              "Adaptability to Work Environment Preferences": number,
              "Problem-Solving and Decision-Making Style": number
            },
            "CulturalFitSummary": string
          },
          "AttitudeSkill": {
            "AttitudeScore": number,
            "AttitudeDetailScoring": {
              "Professionalism": number,
              "Positivity and Enthusiasm": number,
              "Resilience and Response to Challenges": number,
              "Motivation and Work Ethic": number
            },
            "AttitudeSummary": string
          },
          "CommunicationSkill": {
            "CommunicationSkillScore": number,
            "CommunicationSkillDetailScoring": {
              "Clarity, Coherence, and Conciseness of Responses": number,
              "Listening and Engagement in Dialogue": number,
              "Written Communication Skills": number,
              "Non-verbal communication": number
            },
            "CommunicationSkillSummary": string
          },
          "AdaptabilitySkill": {
            "AdaptabilityScore": number,
            "AdaptabilityDetailScoring": {
              "Successful Adaptation to Change": number,
              "Responses to Hypothetical Scenarios": number,
              "Learning and Applying Feedback": number,
              "Feedback from References on Adaptability and Problem-solving": number
            },
            "AdaptabilitySummary": string
          }
        },
        "MBTISummary": string,
        "FeedbackForCandidate": {
          "Strength": {
            "Strength 1": string,
            "Strength 2": string,
            "Strength 3": string
          },
          "WeaknessAndAreasForImprovement": {
            "Weakness 1": string,
            "Weakness 2": string,
            "Weakness 3": string
          },
          "OtherRecommendedJobPosition": {
            "Job Position 1": string,
            "Job Position 2": string,
            "Job Position 3": string
          }
        },
        "OverallEvaluationAndReccomendation": {
          "Summary": string,
          "Recommendation": string
        }
      }

}

// interface PDFFileTSXProps {
//     info: info[];
// }


interface information{
    "InterveweeName": string,
    "InterviewPosition": string,
    "InterviewDate": string,
    "RadarChartSummary": string,
    "TechnicalSkill": {
        "TechnicalSkillScore": number,
        "TechnicalSkillSummary": string,
    },
    "SoftSkill": {
        "PreparationSkill": {
            "PreparationScore": number,
            "PreparationDetailScoring": {
                "Knowledge of the Company, Role, and Industry": number,
                "Quality of Questions for the Interviewer": number,
                "Alignment of Skills and Experiences with Job Requirements": number,
                "Formal and Appropriate Attire": number,
                "Grooming and Tidiness": number,
            },
            "PreparationSummary": string,
        },
        "CulturalFitSkill": {
            "CulturalFitScore": number,
            "CulturalFitDetailScoring": {
                "Alignment with Core Company Values": number,
                "Professionalism and Work Ethic": number,
                "Teamwork and Collaboration Style": number,
                "Adaptability to Work Environment Preferences": number,
                "Problem-Solving and Decision-Making Style": number,
            },
            "CulturalFitSummary": string,
        },
        "AtitudeSkill": {
            "AtitudeScore": number,
            "AtitudeDetailScoring": {
                "Professionalism": number,
                "Positivity and Enthusiasm": number,
                "Resilience and Response to Challenges": number,
                "Motivation and Work Ethic": number,
            },
            "AtitudeSummary": string,
        },
        "CommunicationSkill": {
            "CommunicationSkillScore": number,
            "CommunicationSkillDetailScoring": {
                "Clarity, Coherence, and Conciseness of Responses": number,
                "Listening and Engagement in Dialogue": number,
                "Written Communication Skills": number,
                "Non-verbal communication": number,
            },
            "CommunicationSkillSummary": string,
        },
        "AdaptabilitySkill": {
            "AdaptabilityScore": number,
            "AdaptabilityDetailScoring": {
                "Successful Adaptation to Change": number,
                "Responses to Hypothetical Scenarios": number,
                "Learning and Applying Feedback": number,
                "Feedback from References on Adaptability and Problem-solving": number,
            },
            "AdaptabilitySummary": string,
        },
    },
    "MBTISummary": string,
    "FeedbackForCandidate": {
        "Strength": string[],
        "WeaknessAndAreasForDevelopment": string[],
        "OtherRecommendedJobPosition": string[],
    },

}

// interface PDFFileTSXProps {
//     info: info[];
// }


const PDFFileTSX = ()  => {
    // const [info, setInfo] = useState<any>();
    
    // useEffect(() => {
    //     const getReportInfo = async () => {
    //         const response = await fetch('http://localhost:8000/get-report-data');
    //         const body = await response.json();
    //         console.log("Body is ",body)
    //         setInfo(body) // Update the type of setInfo to accept a single object instead of an array
    
    //         // if (response.status !== 200) {
    //         //     throw Error(body.message) 
    //         // }

    //     }

    //     getReportInfo();
    // }, [])

    // if (!info) {
    //     console.log("Info Have nothing")
    //     return <div>Loading...</div>
    // }

    return(
        // <Document title='Interview Performance Report'>
        //     <Page size="A4" style={styles.page}>
        //         <View style={styles.body}>
        //             <View style={styles.reportTitle}>
        //                 <Text>
        //                     Interviewee Performance Report
        //                 </Text>
        //             </View>

        //             <NormalText text={"Interviewee Name: " + info.InterveweeName }/>

        //             <NormalText text={"Position Applied For: " + info?.InterviewPosition}/>

        //             <NormalText text={"Interview Date: " + info?.InterviewDate}/>

        //             <SubTitle text="Overview of the Interviewee's Performance"/>

        //             <View style={styles.charts}>
        //                 <Image src={`data:image/jpeg;base64,${info.RadarChartBinaryArray}`}/>
        //             </View>

        //             <NormalText text= {info.aiReport.RadarChartSummary}/>

        //             <SubTitle text="Technical Assessment"/>

        //             <SupBoldText text={"Technical Skill Rating: "+ info.aiReport.TechnicalSkill.TechnicalSkillScore + "/5"}/>

        //             <BoldText text="Assessment Summary:"/>                                        

        //             <NormalText text={info.aiReport.TechnicalSkill.TechnicalSkillSummary}/>

        //             <SubTitle text="Soft Skills Assessment"/>

        //             <SupBoldText text={"Preparation Mark:" + info.aiReport.SoftSkill.PreparationSkill.PreparationScore+ "/5"}/>

        //             <BulletNormalText text={"Knowledge of the Company, Role, and Industry :"  + info.aiReport.SoftSkill.PreparationSkill.PreparationDetailScoring['Knowledge of the Company, Role, and Industry']}/>

        //             <BulletNormalText text={"Quality of Questions for the Interviewer :"  + info.aiReport.SoftSkill.PreparationSkill.PreparationDetailScoring['Quality of Questions for the Interviewer']} />

        //             <BulletNormalText text={"Alignment of Skills and Experiences with Job Requirements :"  + info.aiReport.SoftSkill.PreparationSkill.PreparationDetailScoring['Alignment of Skills and Experiences with Job Requirements']}/>

        //             <BulletNormalText text={"Formal and Appropriate Attire :"  + info.aiReport.SoftSkill.PreparationSkill.PreparationDetailScoring['Formal and Appropriate Attire']}/>

        //             <BulletNormalText text={"Grooming and Tidiness :"  + info.aiReport.SoftSkill.PreparationSkill.PreparationDetailScoring['Grooming and Tidiness']}/>

        //             <BlankLine/>

        //             <BoldText text="Assessment Summary:"/>  

        //             <NormalText text= {info.aiReport.SoftSkill.PreparationSkill.PreparationSummary}/>

        //             <SeperateLine />

        //             <SupBoldText text={"Cultural Fit Mark:" +info.aiReport.SoftSkill.CulturalFitSkill.CulturalFitScore+ "/5"}/>

        //             <BulletNormalText text={"Alignment with Core Company Values: " + info.aiReport.SoftSkill.CulturalFitSkill.CulturalFitDetailScoring['Alignment with Core Company Values']} />

        //             <BulletNormalText text={"Professionalism and Work Ethic: " + info.aiReport.SoftSkill.CulturalFitSkill.CulturalFitDetailScoring['Professionalism and Work Ethic']}  />

        //             <BulletNormalText text={"Teamwork and Collaboration Style: " + info.aiReport.SoftSkill.CulturalFitSkill.CulturalFitDetailScoring['Teamwork and Collaboration Style']} />

        //             <BulletNormalText text={"Adaptability to Work Environment Preferences:  " + info.aiReport.SoftSkill.CulturalFitSkill.CulturalFitDetailScoring['Adaptability to Work Environment Preferences']} />

        //             <BulletNormalText text={"Problem-Solving and Decision-Making Style: " + info.aiReport.SoftSkill.CulturalFitSkill.CulturalFitDetailScoring['Problem-Solving and Decision-Making Style']} />

        //             <BlankLine/>

        //             <BoldText text="Assessment Summary:"/>  

        //             <NormalText text={info.aiReport.SoftSkill.CulturalFitSkill.CulturalFitSummary}/>

        //             <SeperateLine />

        //             <SupBoldText text={"Attitude Mark: " + info.aiReport.SoftSkill.AttitudeSkill.AttitudeScore +"/5"}/>

        //             <BulletNormalText text={"Professionalism: " + info.aiReport.SoftSkill.AttitudeSkill.AttitudeDetailScoring.Professionalism}/>

        //             <BulletNormalText text={"Positivity and Enthusiasm: " + info.aiReport.SoftSkill.AttitudeSkill.AttitudeDetailScoring['Positivity and Enthusiasm']} />

        //             <BulletNormalText text={"Resilience and Response to Challenges: " + info.aiReport.SoftSkill.AttitudeSkill.AttitudeDetailScoring['Resilience and Response to Challenges']}/>

        //             <BulletNormalText text={"Motivation and Work Ethic: " + info.aiReport.SoftSkill.AttitudeSkill.AttitudeDetailScoring['Motivation and Work Ethic']}/>

        //             <BlankLine/>

        //             <BoldText text="Assessment Summary:"/>  

        //             <NormalText text={info.aiReport.SoftSkill.AttitudeSkill.AttitudeSummary}/>

        //             <SeperateLine />

        //             <SupBoldText text={"Communication Skill Mark: " + info.aiReport.SoftSkill.CommunicationSkill.CommunicationSkillScore +"/5"}/>

        //             <BulletNormalText text={"Clarity, Coherence, and Conciseness of Responses: " + info.aiReport.SoftSkill.CommunicationSkill.CommunicationSkillDetailScoring['Clarity, Coherence, and Conciseness of Responses']}/>

        //             <BulletNormalText text={"Listening and Engagement in Dialogue: " + info.aiReport.SoftSkill.CommunicationSkill.CommunicationSkillDetailScoring['Listening and Engagement in Dialogue']} />

        //             <BulletNormalText text={"Written Communication Skills: " + info.aiReport.SoftSkill.CommunicationSkill.CommunicationSkillDetailScoring['Written Communication Skills']}/>

        //             <BulletNormalText text={"Non-verbal communication: " + info.aiReport.SoftSkill.CommunicationSkill.CommunicationSkillDetailScoring['Non-verbal communication']}/>

        //             <BlankLine/>

        //             <BoldText text="Assessment Summary:"/>  

        //             <NormalText text={info.aiReport.SoftSkill.CommunicationSkill.CommunicationSkillSummary}/>

        //             <SeperateLine />                    

        //             <SupBoldText text={"Adaptability Mark: " + info.aiReport.SoftSkill.AdaptabilitySkill.AdaptabilityScore + "/5"}/>

        //             <BulletNormalText text={"Successful Adaptation to Change: " + info.aiReport.SoftSkill.AdaptabilitySkill.AdaptabilityDetailScoring['Successful Adaptation to Change']}/>

        //             <BulletNormalText text={"Responses to Hypothetical Scenarios: " + info.aiReport.SoftSkill.AdaptabilitySkill.AdaptabilityDetailScoring['Responses to Hypothetical Scenarios']} />

        //             <BulletNormalText text={"Learning and Applying Feedback: " + info.aiReport.SoftSkill.AdaptabilitySkill.AdaptabilityDetailScoring['Learning and Applying Feedback']}/>

        //             <BulletNormalText text={"Feedback from References on Adaptability and Problem-solving: " + info.aiReport.SoftSkill.AdaptabilitySkill.AdaptabilityDetailScoring['Feedback from References on Adaptability and Problem-solving']}/>

        //             <BlankLine/>

        //             <BoldText text="Assessment Summary:"/>  

        //             <NormalText text={info.aiReport.SoftSkill.AdaptabilitySkill.AdaptabilitySummary}/>

        //             <SeperateLine />     

        //             <SubTitle text="MBTI Personality Assessment in Workplace"/>

        //             <View>
        //                 <Image src = {`data:image/png;base64,${info.MBTIBinaryArray}`}/>
        //             </View>

        //             <NormalText text={info.aiReport.MBTISummary}/>

        //             <SubTitle text="Overall Evaluation and Recommendation"/>

        //             <SupBoldText text="Feedback for Candidate"/>

        //             <BoldText text="Strengths:"/>

        //             <View render={() => Object.values(info.aiReport.FeedbackForCandidate.Strength).map((strength: string | any) => (
        //                 <BulletNormalText text={strength}/>
        //             ))}/>
        //             <BlankLine/>
                    
        //             <BoldText text="Weakness and Areas for Improvement:"/>

        //             <View render={() => Object.values(info.aiReport.FeedbackForCandidate.WeaknessAndAreasForImprovement).map((Weakness: string | any) => (
        //                 <BulletNormalText text={Weakness}/>
        //             ))}/>

        //             <BlankLine/>
                    
        //             <BoldText text = "Other Recommended Job Positions:"/>

        //             <View render={() => Object.values(info.aiReport.FeedbackForCandidate.OtherRecommendedJobPosition).map((Position: string | any) => (
        //                 <BulletNormalText text={Position}/>
        //             ))}/>
        //         </View>
        //     </Page>
        // </Document>

        <Document title='Interview Performance Report'>
        <Page size="A4" style={styles.page}>
            <View style={styles.body}>
                <View style={styles.reportTitle}>
                    <Text>
                        Interviewee Performance Report
                    </Text>
                </View>

                <NormalText text={"Interviewee Name: " + info.InterveweeName}/>

                <NormalText text={"Position Applied For: " + info.InterviewPosition}/>

                <NormalText text={"Interview Date: " + info.InterviewDate}/>

                <SubTitle text="Overview of the Interviewee's Performance"/>

                <View style={styles.charts}>
                    <Image src = '/images/radar.jpeg'/>
                </View>

                <NormalText text= {info.RadarChartSummary}/>

                <SubTitle text="Technical Assessment"/>

                <SupBoldText text={"Technical Skill Rating: "+ info.TechnicalSkill.TechnicalSkillScore + "/5"}/>

                <BoldText text="Assessment Summary:"/>                                        

                <NormalText text={info.TechnicalSkill.TechnicalSkillSummary}/>

                <SubTitle text="Soft Skills Assessment"/>

                <SupBoldText text={"Preparation Mark:" + info.SoftSkill.PreparationSkill.PreparationScore+ "/5"}/>

                <BulletNormalText text={"Knowledge of the Company, Role, and Industry :"  + info.SoftSkill.PreparationSkill.PreparationDetailScoring['Knowledge of the Company, Role, and Industry']}/>

                <BulletNormalText text={"Quality of Questions for the Interviewer :"  + info.SoftSkill.PreparationSkill.PreparationDetailScoring['Quality of Questions for the Interviewer']} />

                <BulletNormalText text={"Alignment of Skills and Experiences with Job Requirements :"  + info.SoftSkill.PreparationSkill.PreparationDetailScoring['Alignment of Skills and Experiences with Job Requirements']}/>

                <BulletNormalText text={"Formal and Appropriate Attire :"  + info.SoftSkill.PreparationSkill.PreparationDetailScoring['Formal and Appropriate Attire']}/>

                <BulletNormalText text={"Grooming and Tidiness :"  + info.SoftSkill.PreparationSkill.PreparationDetailScoring['Grooming and Tidiness']}/>

                <BlankLine/>

                <BoldText text="Assessment Summary:"/>  

                <NormalText text= {info.SoftSkill.PreparationSkill.PreparationSummary}/>

                <SeperateLine />

                <SupBoldText text={"Cultural Fit Mark:" +info.SoftSkill.CulturalFitSkill.CulturalFitScore+ "/5"}/>

                <BulletNormalText text={"Alignment with Core Company Values: " + info.SoftSkill.CulturalFitSkill.CulturalFitDetailScoring['Alignment with Core Company Values']} />

                <BulletNormalText text={"Professionalism and Work Ethic: " + info.SoftSkill.CulturalFitSkill.CulturalFitDetailScoring['Professionalism and Work Ethic']}  />

                <BulletNormalText text={"Teamwork and Collaboration Style: " + info.SoftSkill.CulturalFitSkill.CulturalFitDetailScoring['Teamwork and Collaboration Style']} />

                <BulletNormalText text={"Adaptability to Work Environment Preferences:  " + info.SoftSkill.CulturalFitSkill.CulturalFitDetailScoring['Adaptability to Work Environment Preferences']} />

                <BulletNormalText text={"Problem-Solving and Decision-Making Style: " + info.SoftSkill.CulturalFitSkill.CulturalFitDetailScoring['Problem-Solving and Decision-Making Style']} />

                <BlankLine/>

                <BoldText text="Assessment Summary:"/>  

                <NormalText text={info.SoftSkill.CulturalFitSkill.CulturalFitSummary}/>

                <SeperateLine />

                <SupBoldText text={"Attitude Mark: " + info.SoftSkill.AtitudeSkill.AtitudeScore +"/5"}/>

                <BulletNormalText text={"Professionalism: " + info.SoftSkill.AtitudeSkill.AtitudeDetailScoring.Professionalism}/>

                <BulletNormalText text={"Positivity and Enthusiasm: " + info.SoftSkill.AtitudeSkill.AtitudeDetailScoring['Positivity and Enthusiasm']} />

                <BulletNormalText text={"Resilience and Response to Challenges: " + info.SoftSkill.AtitudeSkill.AtitudeDetailScoring['Resilience and Response to Challenges']}/>

                <BulletNormalText text={"Motivation and Work Ethic: " + info.SoftSkill.AtitudeSkill.AtitudeDetailScoring['Motivation and Work Ethic']}/>

                <BlankLine/>

                <BoldText text="Assessment Summary:"/>  

                <NormalText text={info.SoftSkill.AtitudeSkill.AtitudeSummary}/>

                <SeperateLine />

                <SupBoldText text={"Communication Skill Mark: " + info.SoftSkill.CommunicationSkill.CommunicationSkillScore +"/5"}/>

                <BulletNormalText text={"Clarity, Coherence, and Conciseness of Responses: " + info.SoftSkill.CommunicationSkill.CommunicationSkillDetailScoring['Clarity, Coherence, and Conciseness of Responses']}/>

                <BulletNormalText text={"Listening and Engagement in Dialogue: " + info.SoftSkill.CommunicationSkill.CommunicationSkillDetailScoring['Listening and Engagement in Dialogue']} />

                <BulletNormalText text={"Written Communication Skills: " + info.SoftSkill.CommunicationSkill.CommunicationSkillDetailScoring['Written Communication Skills']}/>

                <BulletNormalText text={"Non-verbal communication: " + info.SoftSkill.CommunicationSkill.CommunicationSkillDetailScoring['Non-verbal communication']}/>

                <BlankLine/>

                <BoldText text="Assessment Summary:"/>  

                <NormalText text={info.SoftSkill.CommunicationSkill.CommunicationSkillSummary}/>

                <SeperateLine />                    

                <SupBoldText text={"Adaptability Mark: " + info.SoftSkill.AdaptabilitySkill.AdaptabilityScore + "/5"}/>

                <BulletNormalText text={"Successful Adaptation to Change: " + info.SoftSkill.AdaptabilitySkill.AdaptabilityDetailScoring['Successful Adaptation to Change']}/>

                <BulletNormalText text={"Responses to Hypothetical Scenarios: " + info.SoftSkill.AdaptabilitySkill.AdaptabilityDetailScoring['Responses to Hypothetical Scenarios']} />

                <BulletNormalText text={"Learning and Applying Feedback: " + info.SoftSkill.AdaptabilitySkill.AdaptabilityDetailScoring['Learning and Applying Feedback']}/>

                <BulletNormalText text={"Feedback from References on Adaptability and Problem-solving: " + info.SoftSkill.AdaptabilitySkill.AdaptabilityDetailScoring['Feedback from References on Adaptability and Problem-solving']}/>

                <BlankLine/>

                <BoldText text="Assessment Summary:"/>  

                <NormalText text={info.SoftSkill.AdaptabilitySkill.AdaptabilitySummary}/>

                <SeperateLine />     

                <SubTitle text="MBTI Personality Assessment in Workplace"/>

                <View>
                    <Image src = '/images/MBTI.png'/>
                </View>

                <NormalText text={info.MBTISummary}/>

                <SubTitle text="Overall Evaluation and Recommendation"/>

                <SupBoldText text="Feedback for Candidate"/>

                <BoldText text="Strengths:"/>

                <View render={() => Object.values(info.FeedbackForCandidate.Strength).map((strength: string) => (
                    <BulletNormalText text={strength}/>
                ))}/>
                <BlankLine/>
                
                <BoldText text="Weakness and Areas for Development:"/>

                <View render={() => Object.values(info.FeedbackForCandidate.WeaknessAndAreasForDevelopment).map((Weakness: string) => (
                    <BulletNormalText text={Weakness}/>
                ))}/>

                <BlankLine/>
                
                <BoldText text = "Other Recommended Job Positions:"/>

                <View render={() => Object.values(info.FeedbackForCandidate.OtherRecommendedJobPosition).map((Position: string) => (
                    <BulletNormalText text={Position}/>
                ))}/>
            </View>
        </Page>
    </Document>

    );
}

const PDFView = () => {

    const [client, setClient] = useState(false)

    useEffect(() => {
        setClient(true)
    }, [])

    return(
    <PDFViewer style={{width:'100%', height:'100vh'}}>
        <PDFFileTSX/>
    </PDFViewer>
    )
}

export default PDFView;