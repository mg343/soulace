import streamlit as st
from PIL import Image


st.set_page_config(page_title="Resources")

st.title("Resources")

logo = Image.open('soulaceBG.png')
st.sidebar.image(logo, use_column_width=True)


col1, col2 = st.columns(2)

#######################################
# COLUMN 1
#######################################

col1.subheader('Psychological Disorders')
col1.markdown("""
<div style="background-color: white; padding:20px 20px;">
<a>

[Mental Health America](https://screening.mhanational.org/screening-tools)

[Mayo Clinic](https://www.mayoclinic.org/diseases-conditions/mental-illness/symptoms-causes/syc-20374968)

[American Psychiatric Association](https://www.psychiatry.org/patients-families/warning-signs-of-mental-illness)

[WebMD](https://www.webmd.com/mental-health/mental-health-types-illness)

[Psychology Today](https://www.psychologytoday.com/us/blog/psychiatry-and-society/202204/mental-health-mental-illness-and-everything-in-between)

[MedlinePlus](https://medlineplus.gov/mentaldisorders.html)

[Psych Central](https://psychcentral.com/disorders/)

[Mental Health First Aid](https://www.mentalhealthfirstaid.org/mental-health-resources/)

[National Alliance on Mental Illness](https://www.nami.org/Learn-More/Mental-Health-Conditions)


</a>
</div>
""", unsafe_allow_html = True)

col1.markdown("""                   """)

col1.subheader('Substance Use')
col1.markdown("""
<div style="background-color: white; padding:20px 20px;">
<a>

[DEA Recovery](https://www.dea.gov/recovery-resources)

[Alcoholics Anonymous](https://www.aa.org/pages/en_US/information-on-alcoholics-anonymous)

[Federal Alcohol Abuse Resource Collection](https://nasadad.org/federal-resources/)

[SAMHSA](https://www.samhsa.gov/find-help/national-helpline)

[DrugAbuse.gov](https://teens.drugabuse.gov/drug-facts/prescription-drugs)

[American Addiction Centers](https://americanaddictioncenters.org/online-resources)

[Alcohol Abuse and Alcoholism](https://www.niaaa.nih.gov/publications/brochures-and-fact-sheets)


</a>
</div>
""", unsafe_allow_html = True)

col1.markdown("""                   """)

col1.subheader('Emotional Well-Being')
col1.markdown("""
<div style="background-color: white; padding:20px 20px;">
<a>

[Mind](https://www.mind.org.uk/information-support/tips-for-everyday-living/wellbeing/wellbeing/)

[National Institutes of Health](https://www.nih.gov/health-information/emotional-wellness-toolkit-more-resources)

[Well Being Trust](https://wellbeingtrust.org/resources/mental-health-resources/)

[UCSF Emotional Resources](https://coronavirus.ucsf.edu/emotional-health-and-well-being-resources)

[Blue Cross Blue Shield](https://www.anthem.com/mental-health)

[World Health Organization](https://www.who.int/news-room/feature-stories/mental-well-being-resources-for-the-public)


</a>
</div>
""", unsafe_allow_html = True)










#######################################
# COLUMN 2
#######################################

# Display interactive widgets

col2.subheader('Stress and Coping')
col2.markdown("""
<div style="background-color: white; padding:20px 20px;">
<a>

[Mayo Clinic](https://www.mayoclinic.org/healthy-lifestyle/stress-management/in-depth/stress-management/art-20044289)

[Healthline](https://www.healthline.com/health/stress)

[American Psychological Association](https://www.apa.org/topics/stress)

[Verywell Mind](https://www.verywellmind.com/stress-management-4157211)

[HelpGuide](https://www.helpguide.org/articles/stress/stress-management.htm)

[Anxiety and Depression Association](https://adaa.org/living-with-anxiety/managing-anxiety)

[Mind](https://www.mind.org.uk/information-support/tips-for-everyday-living/stress/)

[Centers for Disease Control and Prevention](https://www.cdc.gov/mentalhealth/cope-with-stress/index.html)


</a>
</div>
""", unsafe_allow_html = True)

col2.markdown("""                   """)

col2.subheader('Cognition Patterns')
col2.markdown("""
<div style="background-color: white; padding:20px 20px;">
<a>

[Psych Central - Distortions](https://psychcentral.com/lib/15-common-cognitive-distortions/)

[PysioPedia](https://www.physio-pedia.com/Cognitive_Impairments)

[Harvard Health](https://www.health.harvard.edu/blog/how-to-recognize-and-tame-your-cognitive-distortions-202205042738)

[Parkinson's Foundation](https://www.parkinson.org/blog/tips/mental-health-tips)

[Simply Psychology](https://www.simplypsychology.org/cognitive-therapy.html)

[American Psychological Association](https://www.apa.org/ptsd-guideline/patients-and-families/cognitive-behavioral)

[Psych Central - Therapy](https://psychcentral.com/lib/in-depth-cognitive-behavioral-therapy/)

[Mind](https://www.mind.org.uk/information-support/drugs-and-treatments/cognitive-behavioural-therapy-cbt/about-cbt/)

</a>
</div>
""", unsafe_allow_html = True)

col2.markdown("""                   """)




col2.subheader('Self-Confidence')
col2.markdown("""
<div style="background-color: white; padding:20px 20px;">
<a>

[University of South Florida](https://www.usf.edu/student-affairs/counseling-center/top-concerns/what-is-self-confidence.aspx)

[ADD Association](https://add.org/self-confidence-vs-self-esteem/)

[MindTools](https://www.mindtools.com/ap5omwt/how-to-build-self-confidencel)

[NY Times](https://www.nytimes.com/2019/06/03/smarter-living/how-to-improve-self-confidence.html)

[Princeton UMatter](https://umatter.princeton.edu/respect/tools/self-esteem)

[Mayo Clinic](https://www.mayoclinic.org/healthy-lifestyle/adult-health/in-depth/self-esteem/art-20045374)


</a>
</div>
""", unsafe_allow_html = True)