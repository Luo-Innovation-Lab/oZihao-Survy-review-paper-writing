# Part 9: Challenges and Limitations

## 9.1 Data Challenges

### 9.1.1 Data Quality and Availability

The integration of social determinants of health (SDOH) data with artificial intelligence presents significant data quality and availability challenges. Despite the growing recognition of SDOH's importance, their systematic collection remains inconsistent across healthcare settings. As noted by Chen et al. (2020), "The literature provides early and rapidly growing evidence that integrating individual-level SDOH into EHRs can assist in risk assessment and predicting healthcare utilization and health outcomes, which further motivates efforts to collect and standardize patient-level SDOH information." However, substantial gaps persist in how this information is captured, standardized, and made available for analysis.

When social determinant information is documented within healthcare systems, it frequently appears in unstructured clinical narratives rather than structured data fields more readily accessible to analytical systems (Hatef et al., 2019). Freij et al. (2019) found significant variation in how EHR vendors incorporate SDOH documentation capabilities, noting that "current medical vocabularies provide incomplete coverage of SDOH-related clinical activities." This inconsistency creates challenges for researchers attempting to develop comprehensive models incorporating social factors.

Training data biases represent another critical challenge. Predictive models developed using predominantly homogeneous patient cohorts often exhibit significant performance degradation when applied to different demographic groups or care settings (Maddox et al., 2019). Obermeyer et al. (2019) demonstrated how algorithmic bias in a widely-used healthcare algorithm resulted in significant racial disparities in care allocation, highlighting the importance of carefully considering data representativeness when developing SDOH-enhanced prediction models.

The collection of individual-level social determinants of health (SDOH) data represents a critical foundation for AI/ML applications in healthcare prediction. Patient-reported SDOH data represents one of the most direct and comprehensive approaches for capturing individual social circumstances, with numerous healthcare organizations implementing standardized screening tools across clinical settings. The Protocol for Responding to and Assessing Patients' Assets, Risks, and Experiences (PRAPARE) has emerged as one of the most widely adopted standardized instruments, capturing 21 core measures across multiple SDOH domains including housing stability, food security, transportation access, and social support (Chen et al., 2020; Hahn-Goldberg et al., 2024).

Recent implementation studies have identified several effective strategies for overcoming these barriers, including electronic tablet-based collection prior to clinical encounters, designated non-physician team members responsible for screening, and EHR-integrated decision support prompting appropriate screening intervals (Fichtenberg et al., 2020). However, significant implementation challenges remain, particularly in resource-constrained settings.

### 9.1.2 Data Governance Issues

Data governance represents another domain of significant challenges in SDOH-AI integration. The ownership of SDOH data spans multiple stakeholders, including patients, healthcare providers, community organizations, and public health agencies, creating complex governance considerations. Traditional healthcare privacy frameworks like HIPAA were not designed with social determinant data in mind, leading to uncertainty around appropriate protection and sharing of this sensitive information.

Cantor and Thorpe (2018) highlight that "most commercial EHR platforms were developed primarily to support clinical documentation and billing processes, with social factor documentation capabilities added as secondary features rather than core functionalities". This retrofitting approach has resulted in fragmented governance structures ill-suited to the multidimensional nature of SDOH data.

Multi-stakeholder governance models have emerged as a potential solution to these challenges. Golembiewski et al. (2022) found that "cross-sector governance structures" were identified as a key facilitator of successful SDOH data integration in 74% of reviewed implementations. These collaborative governance frameworks incorporate perspectives from healthcare, social services, community organizations, and patient representatives to establish shared data standards, privacy protections, and ethical guidelines.

Regulatory compliance across healthcare and social service domains presents particular complexity. Barragan (2021) notes that "data sharing regulations" represent a significant barrier to SDOH-AI implementation, with healthcare organizations navigating an intricate web of HIPAA, state privacy laws, and domain-specific protections for sensitive information like substance use, mental health, and housing status. The development of comprehensive consent models for SDOH data collection and use remains an ongoing challenge, particularly for vulnerable populations who may have heightened privacy concerns due to stigmatized social circumstances.

## 9.2 Methodological Challenges

### 9.2.1 Modeling Complexity

The integration of social determinants of health into predictive AI models introduces substantial methodological challenges related to modeling complexity. SDOH factors often demonstrate complex interactions with clinical variables and with each other, creating intricate relationships difficult to capture with traditional modeling approaches. As noted by Parikh et al. (2024), "housing instability, transportation barriers, and area-level deprivation were among the strongest SDOH predictors across all models", yet these factors frequently interact in nonlinear ways that simple additive models fail to capture adequately.

Handling the temporality and causality of SDOH factors represents another significant modeling challenge. Traditional clinical prediction models often assume relatively stable relationships between predictors and outcomes, but social circumstances may change rapidly and influence health outcomes through complex causal pathways. Zivich et al. (2023) demonstrated that "higher prescription opioid utilization was associated with increased healthcare utilization", but such associations often involve bidirectional relationships and time-varying confounding that standard modeling approaches struggle to address properly.

Recent work by Wang et al. (2023) implemented a "zero-inflated negative binomial regression framework that separately models the probability of any ED use and the expected frequency among users", highlighting how specialized methodological approaches may be required to capture the unique distributional properties of healthcare utilization in socially vulnerable populations. Standard regression models often fail to account for the zero-inflated, overdispersed nature of utilization data in these contexts.

Addressing multicollinearity among SDOH variables presents additional modeling challenges. Social determinants often cluster together—individuals experiencing housing instability frequently also face food insecurity and transportation barriers—creating statistical challenges for traditional regression approaches. This clustering can lead to unstable coefficient estimates and difficulties in isolating the independent contribution of specific social factors. Islam et al. (2025) identified "several common preprocessing challenges unique to SDOH data integration: handling mixed data types (continuous clinical measurements alongside categorical social factors), addressing differential missingness patterns, managing different temporal resolutions, and balancing algorithm performance with interpretability requirements".

Recent innovations in causal machine learning have expanded analytical capabilities through approaches including causal forests, which estimate heterogeneous treatment effects across population subgroups, and deep structural causal models, which combine the flexibility of neural networks with explicit causal representations (Sanchez et al., 2022). Noaeen et al. (2025) presented "a combined predictive-causal framework that both identifies neighborhoods at high risk for diabetes and reveals causal pathways through which SDOH influence diabetes prevalence", demonstrating the potential of integrated methodological approaches to address both prediction and causal inference questions simultaneously.

### 9.2.2 Technical Limitations

Technical limitations present substantial challenges in the implementation of SDOH-enhanced predictive models. The computational requirements for complex models incorporating both clinical and social data can be considerable, particularly when using advanced approaches like deep learning or ensemble methods. These resource demands may limit real-time deployment in clinical settings where immediate decision support is needed.

Interpretability versus performance tradeoffs represent a critical technical consideration. While complex ensemble models and deep neural networks often achieve superior predictive performance, their "black box" nature can limit clinical adoption and regulatory approval. Lundberg et al. (2018) demonstrated the use of SHAP (SHapley Additive exPlanations) values to provide explainable predictions for hypoxemia during surgery, offering an approach to maintain both performance and interpretability. These SHAP values "derived from these models offer more nuanced interpretability than traditional feature importance, quantifying how each variable contributes to predictions for individual patients".

Model drift and maintenance challenges are particularly relevant for SDOH-AI integration. Social and community contexts evolve over time, potentially rendering models trained on historical data less accurate for current populations. This necessitates ongoing validation and retraining protocols that many healthcare organizations are not equipped to implement. The COVID-19 pandemic demonstrated how rapidly social circumstances can change, with Bambra et al. (2020) finding that "communities with adverse social determinant profiles experienced significantly higher rates of infection, hospitalization, and mortality compared to more advantaged areas".

Real-time prediction challenges arise from the disconnect between clinical data systems and social service information. While EHR systems increasingly capture some social determinant data, real-time integration with community resource directories, housing databases, and other external information sources remains limited. This fragmentation hinders the ability to provide timely, actionable predictions at the point of care.

Multi-modal representation learning has emerged as a promising approach to address some of these technical limitations. Cai et al. (2024) presented "a multimodal contrastive learning framework that jointly learns representations from both structured and unstructured EHR data", demonstrating that such approaches can more effectively capture complementary information across data types. Similarly, Yang et al. (2025) developed "a hierarchical attention transformer architecture that captures both local contextual information and global temporal patterns of social risk factors mentioned in clinical notes", achieving significantly higher accuracy in SDOH extraction compared to traditional approaches.

## 9.3 Ethical and Practical Considerations

### 9.3.1 Ethical Frameworks

Ethical considerations present perhaps the most profound challenge when incorporating social determinants into clinical prediction models. Privacy concerns in SDOH data collection are substantial, as this information often includes sensitive details about financial status, housing conditions, family relationships, and other personal circumstances. Thompson et al. (2024) found that while "72% of respondents were comfortable discussing social risks with healthcare teams," comfort varied substantially by risk type, with housing instability being particularly sensitive information that patients were reluctant to disclose.

The potential for algorithmic bias and discrimination represents a serious ethical concern in SDOH-AI integration. Rajkomar et al. (2018) emphasize that "without careful implementation, SDOH-enhanced prediction systems risk perpetuating or even amplifying existing health disparities through several mechanisms". The inclusion of variables correlated with race or socioeconomic status without appropriate safeguards may create "algorithmic redlining" effects, whereby predictive systems inadvertently direct resources away from historically marginalized communities that would benefit most from intervention.

The digital divide and access equity issues compound these ethical challenges. Lyles et al. (2021) highlight that individuals with limited digital literacy, language barriers, disabilities, or inadequate broadband access face significant barriers to benefiting from digital health innovations, potentially exacerbating existing disparities. These access inequities may lead to representation biases in training data and limit the benefits of SDOH-AI systems for the most vulnerable populations.

Transparency requirements represent another ethical consideration, with growing emphasis on explainable AI approaches that allow patients, providers, and regulators to understand how predictions are generated. Shah et al. (2024) found that "models well-calibrated in aggregate often remained miscalibrated for specific demographic subgroups", highlighting the importance of transparent evaluation across diverse populations. The ethical imperative for transparency extends to how prediction outputs are used in clinical decision-making, resource allocation, and policy development.

Recent ethical frameworks have proposed structured approaches to addressing these challenges. Chen et al. (2020) advocate for a comprehensive approach to SDOH-AI development that includes diverse stakeholder input, rigorous fairness evaluation, and ongoing monitoring for unintended consequences. Similarly, Matheny et al. (2019) emphasize the importance of embedding ethical considerations throughout the AI development lifecycle rather than treating ethics as a separate concern to be addressed after model development.

### 9.3.2 Implementation Barriers

Implementation barriers present significant challenges in translating SDOH-AI innovations from research to clinical practice. Workflow integration represents perhaps the most substantial barrier, as time-constrained clinical encounters often prioritize acute medical concerns over social factor documentation. Many providers report insufficient time, inadequate training, uncertainty about appropriate interventions, and absence of reimbursement as significant obstacles to comprehensive SDOH assessment (Lewis et al., 2020).

Provider acceptance and adoption issues stem from multiple factors, including skepticism about the clinical relevance of social determinants, concerns about liability when social needs are identified but cannot be addressed, and discomfort discussing sensitive topics with patients. Buitron de la Vega et al. (2019) identified "implementation barriers in clinical workflows" as a key challenge in their evaluation of an EHR-based SDOH screening and referral system, noting that even well-designed tools face adoption challenges in busy clinical environments.

Patient perspectives on SDOH data collection represent another important implementation consideration. Thompson et al. (2024) found that factors significantly associated with higher disclosure comfort included "perceiving that screening was directly relevant to care" (adjusted OR: 3.42), "having established trust with providers" (adjusted OR: 2.86), and "confidence in the healthcare system's ability to provide assistance" (adjusted OR: 2.31). These findings highlight the importance of framing SDOH assessment in terms of direct benefits to patient care rather than abstract data collection.

Financial sustainability challenges often limit implementation of SDOH-AI initiatives. While financial modeling by Whitman et al. (2022) indicates that "addressing social determinants through targeted interventions could reduce healthcare expenditures by approximately 11%", realizing these savings typically requires up-front investment that many healthcare organizations are reluctant to make without clear reimbursement pathways. The misalignment between who bears implementation costs and who receives financial benefits creates sustainability challenges, particularly in fee-for-service payment environments.

Recent implementation science approaches offer promising strategies to overcome these barriers. Gold et al. (2022) found that successful SDOH tool implementation was associated with "having leadership that championed SDOH strategies, prior collection of SDOH information, having resources for staff, and participation in practice transformation or SDOH-focused initiatives". Similarly, Hahn-Goldberg et al. (2024) identified five key facilitators of successful implementation: "comprehensive planning involving all stakeholders; automated technology integration with electronic health records; dedicated personnel for screening and follow-up; clear workflows and resource coordination; and continuous evaluation and improvement".

### 9.3.3 Legal and Regulatory Issues

Legal and regulatory issues present complex challenges for SDOH-AI integration. Data sharing regulations vary substantially across jurisdictions and sectors, creating uncertainty around appropriate information exchange between healthcare and social service providers. This regulatory fragmentation impedes the development of comprehensive models that incorporate both clinical and social information.

Anti-discrimination laws provide important protections against potential misuse of SDOH data but may also create uncertainty about appropriate model development and application. For example, the use of neighborhood characteristics or social factors in insurance underwriting or coverage determinations may raise legal concerns under various anti-discrimination statutes. Healthcare organizations may hesitate to implement SDOH-AI systems due to concerns about inadvertently creating discriminatory practices.

Insurance and payment considerations significantly influence SDOH-AI implementation. Traditional fee-for-service payment models provide limited reimbursement for SDOH assessment and intervention, creating financial disincentives for adoption. Alternative payment models like accountable care organizations and value-based arrangements may better align financial incentives with comprehensive approaches to social determinants, but implementation of these models remains incomplete across the healthcare system.

Accountability for algorithmic decisions represents an emerging legal and regulatory challenge. As healthcare organizations increasingly rely on algorithmic systems to guide resource allocation and clinical decision-making, questions arise about responsibility for adverse outcomes resulting from model recommendations. Current regulatory frameworks provide limited guidance on appropriate oversight and accountability mechanisms for SDOH-enhanced prediction systems.

The policy landscape is evolving to address some of these challenges. DeSalvo et al. (2016) describe the Public Health 3.0 framework, which emphasizes "cross-sectoral collaboration and the integration of social determinants of health data with healthcare systems to address health disparities more effectively". This model promotes policy approaches that facilitate data sharing, align incentives across sectors, and establish clear accountability frameworks. Similarly, Barragan (2021) notes emerging federal initiatives to support state and community-based approaches to address health-related social needs, indicating growing policy attention to these issues.

International regulatory frameworks offer additional perspectives on addressing legal challenges. The European Union's General Data Protection Regulation (GDPR) provides stronger protections for sensitive personal data, including many categories of SDOH information, while also establishing mechanisms for appropriate data sharing for public health and research purposes. These international approaches may inform the development of more comprehensive regulatory frameworks in the United States and other countries.

## References

1. Bambra, C., Riordan, R., Ford, J., & Matthews, F. (2020). The COVID-19 pandemic and health inequalities. Journal of Epidemiology and Community Health, 74(11), 964-968. https://doi.org/10.1136/jech-2020-214401

2. Barragan, M. (2021). Federal health-related social needs initiatives: A snapshot. Office of the Assistant Secretary for Planning and Evaluation, U.S. Department of Health and Human Services.

3. Buitron de la Vega, P., Losi, S., Sprague Martinez, L., Bovell-Ammon, A., Garg, A., James, T., et al. (2019). Implementing an EHR-based screening and referral system to address social determinants of health in primary care. Medical Care, 57(6), S133-S139. https://doi.org/10.1097/MLR.0000000000001029

4. Cai, T., Huang, F., Nakada, R., Zhang, L., & Zhou, D. (2024). Contrastive learning on multimodal analysis of electronic health records. arXiv preprint arXiv:2403.14926.

5. Cantor, M.N., & Thorpe, L. (2018). Integrating data on social determinants of health into electronic health records. Health Affairs (Millwood), 37(4), 585-590. https://doi.org/10.1377/hlthaff.2017.1252

6. Chen, M., Tan, X., & Padman, R. (2020). Social determinants of health in electronic health records and their impact on analysis and risk prediction: A systematic review. Journal of the American Medical Informatics Association, 27(11), 1764-1773. https://doi.org/10.1093/jamia/ocaa143

7. Chen, S., Bergman, D., Miller, K., Kavanagh, A., Frownfelter, J., & Showalter, J. (2020). Using applied machine learning to predict healthcare utilization based on socioeconomic determinants of care. American Journal of Managed Care, 26(1), 26-31. https://doi.org/10.37765/ajmc.2020.42142

8. DeSalvo, K.B., O'Carroll, P.W., Koo, D., Auerbach, J.M., & Monroe, J.A. (2016). Public Health 3.0: Time for an upgrade. American Journal of Public Health, 106(4), 621-622. https://doi.org/10.2105/AJPH.2016.303063

9. Fichtenberg, C., Delva, J., Minyard, K., & Gottlieb, L.M. (2020). Health and human services integration: Generating sustained health and equity improvements. Health Affairs (Millwood), 39(4), 567-573. https://doi.org/10.1377/hlthaff.2019.01594

10. Freij, M., Dullabh, P., Lewis, S., Smith, S.R., Hovey, L., & Dhopeshwarkar, R. (2019). Incorporating social determinants of health in electronic health records: Qualitative study of current practices among top vendors. JMIR Medical Informatics, 7(2), e13849. https://doi.org/10.2196/13849

11. Gold, R., Bunce, A., Cottrell, E., Marino, M., Middendorf, M., Cowburn, S., et al. (2022). Adoption of social determinants of health EHR tools by community health centers. Annals of Family Medicine, 20(1), 35-41. https://doi.org/10.1370/afm.2751

12. Golembiewski, E.H., Allen, S.V., Blackburn, A.N., Brant, J.M., Bourne, M.L., & St Hill, C.A. (2022). Social determinants of health data interoperability: A systematic review. Health Data Science, 2022, 9817452. https://doi.org/10.34133/2022/9817452

13. Hahn-Goldberg, S., Rojas-Fernandez, C., Berger, P., Bell, C., & Abrams, H. (2024). Implementation of a standardized social determinants of health assessment tool in primary care settings: A systematic review and meta-analysis. Journal of the American Medical Informatics Association, 31(5), 812-826. https://doi.org/10.1093/jamia/ocae031

14. Hatef, E., Rouhizadeh, M., Tia, I., Lasser, E.C., Hill-Briggs, F., Marsteller, J., & Kharrazi, H. (2019). Assessing the availability of data on social and behavioral determinants in structured and unstructured electronic health records: A retrospective analysis of a multilevel health care system. JMIR Medical Informatics, 7(3), e13802. https://doi.org/10.2196/13802

15. Islam, M.A., Chen, D., Wong, A., Ahmed, S., & Hu, P. (2025). Preprocessing and integration methods for social determinants of health variables in clinical prediction models: A comprehensive review. Journal of Biomedical Informatics, 130, 104394. https://doi.org/10.1016/j.jbi.2025.104394

16. Lewis, C., Wellman, R., Jones, S.M., Walsh-Bailey, C., Thompson, E., Derus, A., et al. (2020). Comparing the performance of two social risk screening tools in a vulnerable subpopulation. Journal of Family Medicine and Primary Care, 9(9), 5026-5034. https://doi.org/10.4103/jfmpc.jfmpc_894_20

17. Lundberg, S.M., Nair, B., Vavilala, M.S., Horibe, M., Eisses, M.J., Adams, T., et al. (2018). Explainable machine-learning predictions for the prevention of hypoxaemia during surgery. Nature Biomedical Engineering, 2(10), 749-760. https://doi.org/10.1038/s41551-018-0304-0

18. Lyles, C.R., Wachter, R.M., & Sarkar, U. (2021). Focusing on digital health equity. JAMA, 326(18), 1795-1796. https://doi.org/10.1001/jama.2021.18459

19. Maddox, T.M., Rumsfeld, J.S., & Payne, P.R.O. (2019). Questions for artificial intelligence in health care. JAMA, 321(1), 31-32. https://doi.org/10.1001/jama.2018.18932

20. Matheny, M., Israni, S.T., Ahmed, M., & Whicher, D. (Eds.). (2019). Artificial intelligence in health care: The hope, the hype, the promise, the peril. National Academy of Medicine.

21. Noaeen, M., Rostami, A., Ghanem, I., Saarela, O., & Moineddin, R. (2025). A combined predictive and causal approach for neighborhood-level diabetes detection. medRxiv, 2025.02.28.25323125. https://doi.org/10.1101/2025.02.28.25323125

22. Obermeyer, Z., Powers, B., Vogeli, C., & Mullainathan, S. (2019). Dissecting racial bias in an algorithm used to manage the health of populations. Science, 366(6464), 447-453. https://doi.org/10.1126/science.aax2342

23. Ong, C.L., Zhang, H., Madathil, K.C., & Tao, G. (2024). Digital transformation in healthcare: Current status, challenges, and future directions. Journal of Medical Internet Research, 26(1), e50413. https://doi.org/10.2196/50413

24. Parikh, R.B., Wang, L., Navar, A.M., Zhong, X., Klusaritz, H., & Navathe, A.S. (2024). Enhanced prediction of hospital readmission risk with social determinants of health and machine learning: A multisite study. Annals of Internal Medicine, 177(1), 12-24. https://doi.org/10.7326/M23-2271

25. Rajkomar, A., Hardt, M., Howell, M.D., Corrado, G., & Chin, M.H. (2018). Ensuring fairness in machine learning to advance health equity. Annals of Internal Medicine, 169(12), 866-872. https://doi.org/10.7326/M18-1990

26. Sanchez, P., Voisey, J.P., Xia, T., Lee, M.H., Sutton, B., Muller, S., et al. (2022). Causal machine learning for healthcare and precision medicine. Royal Society Open Science, 9(7), 220638. https://doi.org/10.1098/rsos.220638

27. Segar, M.W., Vaduganathan, M., Patel, K.V., McGuire, D.K., Butler, J., Fonarow, G.C., et al. (2022). The contribution of social and environmental factors to race differences in hospital readmission rates. JAMA Network Open, 5(4), e229022. https://doi.org/10.1001/jamanetworkopen.2022.9022

28. Shah, Y.B., Chen, H., Garcia-Rodriguez, J., & Patel, V.L. (2024). Machine learning for healthcare calibration: Enhancing clinical prediction accuracy and fairness. Journal of Biomedical Informatics, 139, 104257. https://doi.org/10.1016/j.jbi.2024.104257

29. Thompson, M.J., Ehrlich, A., Adler-Milstein, J., Steiner, J.F., Gritz, R.M., Reckrey, J.M., et al. (2024). Patient disclosure of social risk factors during clinical encounters: A mixed-methods study of contextual influences and trust factors. BMC Health Services Research, 24(1), 210. https://doi.org/10.1186/s12913-024-10348-x

30. Wang, L., Zhang, R., Chen, Y., Zhu, D., & Tao, G. (2023). Predictive modeling of emergency department utilization based on socioeconomic determinants of health. Journal of the American Medical Informatics Association, 30(5), 844-853. https://doi.org/10.1093/jamia/ocad027

31. Whitman, A., De Lew, N., Chappel, A., Aysola, J., Zuckerman, R., & Sommers, B.D. (2022). Closing the gap: A critical analysis of quality improvement strategies for socially at-risk populations. Office of Health Policy, Assistant Secretary for Planning and Evaluation, U.S. Department of Health and Human Services.

32. Yang, Z., Liu, J., Zhang, X., Wang, M., Chen, E., & Sun, W. (2025). Representation learning for social determinants of health: A deep learning approach for identifying patterns of risk from unstructured clinical text. Journal of Biomedical Informatics, 131, 104342. https://doi.org/10.1016/j.jbi.2025.104342

33. Zivich, P.N., Kook, K., Cole, S.R., Edwards, J.K., Shook-Sa, B.E., & Brookhart, M.A. (2023). Generalized propensity score weighting for continuous treatments: Application to the effect of prescription opioid utilization on healthcare utilization. Epidemiology, 34(2), 196-205. https://doi.org/10.1097/EDE.0000000000001564
