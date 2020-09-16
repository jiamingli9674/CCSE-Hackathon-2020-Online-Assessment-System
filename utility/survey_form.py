from wtforms.fields import RadioField, SubmitField
from wtforms.form import Form
from wtforms.validators import DataRequired

class SurveyForm(Form):
    # choice_type_1 = [("Criteria Met", "Criteria Met"), ("Partial Compliance", "Partial Compliance"),("Criteria Not Met", "Criteria Not Met")]
    # choice_type_2 = [("Yes", "Yes"), ("No", "No")]
    choice_type_3 = [("Always", "Always"), ("Almost", "Almost"), ("Never", "Never"), ("Almost Always", "Almost Always"), ("Sometimes", "Sometimes"), ("NA", "NA")]
    
    q_1 = RadioField(label="1.I have a chaperone present during sensitive examinations, regardless of patient gender. ", choices=choice_type_3, validators=[DataRequired()])
    q_2 = RadioField(label="2.The name of the chaperone is documented in the medical record. ", choices=choice_type_3, validators=[DataRequired()])
    # q_3 = RadioField(label="3.Clinical practice guidelines are followed to provide evidence-based care.", choices=choice_type_3, validators=[DataRequired()])
    # q_4 = RadioField(label="4.Vital signs (temperature, blood pressure, heart rate, and respiratory rate) are obtained and documented in the medical record.", choices=choice_type_3, validators=[DataRequired()])      
    # q_5 = RadioField(label="5.My practice follows a specific process to consistently notify patients of abnormal test results and documenting any recommended follow-up testing or treatment in the medical record.", choices=choice_type_3, validators=[DataRequired()])
    # q_6 = RadioField(label="6.I either speak with patients over the phone or they return to the office to discuss the abnormal results.", choices=choice_type_3, validators=[DataRequired()])
    # q_7 = RadioField(label="7.Patients can access their medical record and test results through a patient portal.", choices=choice_type_3, validators=[DataRequired()])
    # q_8 = RadioField(label="8.I stay current on age-appropriate malignancy screening and preventative health measures.", choices=choice_type_3, validators=[DataRequired()])
    # q_9 = RadioField(label="9.I participate in local continuing medical education courses.", choices=choice_type_3, validators=[DataRequired()])
    # q_10 = RadioField(label="10.I participate in national continuing medical education courses.", choices=choice_type_3, validators=[DataRequired()])
    # q_11 = RadioField(label="11.I read medical journals relevant to my practice.", choices=choice_type_3, validators=[DataRequired()])
    # q_12 = RadioField(label="12.I participate in CME courses and read articles provided, free of charge, by MagMutual.", choices=choice_type_3, validators=[DataRequired()])
    # q_13 = RadioField(label="13.A physician or advanced practice clinician conducts informed consent discussions with patients for all invasive procedures or treatments.", choices=choice_type_3, validators=[DataRequired()])
    # q_14 = RadioField(label="14.The informed consent discussion, including risks, benefits, alternatives and patient consent are documented in the medical record.", choices=choice_type_3, validators=[DataRequired()])
    # q_15 = RadioField(label="15.Informed consent forms are signed for invasive procedures and saved in the medical record. ", choices=choice_type_3, validators=[DataRequired()])
    # q_16 = RadioField(label="16.Patient non-compliance and/or informed refusal of care is documented in the medical record.", choices=choice_type_3, validators=[DataRequired()])
    # q_17 = RadioField(label="17.I reach out to The Institute's team of medical, legal and safety experts at MagMutual to assist me with patient safety, regulatory and operational questions.", choices=choice_type_3, validators=[DataRequired()])
    # q_18 = RadioField(label="18.Practice agreements and protocols, consistent with state laws and regulations, for advanced practice clinicians are followed, current and available.", choices=choice_type_3, validators=[DataRequired()])
    # q_19 = RadioField(label="19.Staff members performing procedures (e.g. injections, electrocardiograms) are qualified, trained and competencies are evaluated annually.", choices=choice_type_3, validators=[DataRequired()])
    # q_20 = RadioField(label="20.An internal peer review process is in place that includes provider-to-provider chart audits.", choices=choice_type_3, validators=[DataRequired()])
    # q_21 = RadioField(label="21.I participate in regular meetings within the organization to discuss quality initiatives, risk management and operations.", choices=choice_type_3, validators=[DataRequired()])
    # q_22 = RadioField(label="22.I review and countersign charts of advance practice clinicians I supervise within the same week of service.", choices=choice_type_3, validators=[DataRequired()])
    # q_23 = RadioField(label="23.I have input on whether a staff member is hired or fired at my place of work.", choices=choice_type_3, validators=[DataRequired()])
    # q_24 = RadioField(label="24.I participate in updating the operational policies and procedures of my organization.", choices=choice_type_3, validators=[DataRequired()])
    # q_25 = RadioField(label="25.I feel that I'm compensated appropriately for the job that I do. ", choices=choice_type_3, validators=[DataRequired()])
    # q_26 = RadioField(label="26.A current problem list and medical history is documented in the medical record.", choices=choice_type_3, validators=[DataRequired()])
    # q_27 = RadioField(label="27.Objective findings of the physical exam, including pertinent negatives, are documented in the medical record.", choices=choice_type_3, validators=[DataRequired()])
    # q_28 = RadioField(label="28.A physician or advanced practice clinician reviews all test results, signs and dates the result. For electronic health records, a electronic signature and date stamp is created. ", choices=choice_type_3, validators=[DataRequired()])
    # q_29 = RadioField(label="29.Treatment plans are consistent with working diagnosis and documented in the medical record.", choices=choice_type_3, validators=[DataRequired()])
    # q_30 = RadioField(label="30.How often do you utilize 'cloning', 'copying and pasting' and/or 'pulling forward' to document in the medical record .", choices=choice_type_3, validators=[DataRequired()])
    # q_31 = RadioField(label="31.A current list of medications is documented in the medical record, including over-the-counter and herbal supplements. The list includes medication dose and frequency.", choices=choice_type_3, validators=[DataRequired()])
    # q_32 = RadioField(label="32.The medication list is updated at each office visit and when medications are added/changed/discontinued.", choices=choice_type_3, validators=[DataRequired()])
    # q_33 = RadioField(label="33.Allergies and adverse drug reactions are documented and reviewed prior to prescribing.", choices=choice_type_3, validators=[DataRequired()])
    # q_34 = RadioField(label="34.Patients are informed of the serious side effects from medications with black box warnings.  ", choices=choice_type_3, validators=[DataRequired()])
    # q_35 = RadioField(label="35.Patients are instructed on new medications, especially high-risk medications that could pose a health risk if not taken appropriately and that instruction is documented in the medical record.", choices=choice_type_3, validators=[DataRequired()])
    # q_36 = RadioField(label="36.Patients prescribed new medications are monitored and asked about any side effects or concerns. Response to therapy is documented in the medical record.", choices=choice_type_3, validators=[DataRequired()])
    # q_37 = RadioField(label="37.A physician or advanced practice clinician authorizes all prescription refills or staff utilizes written protocols with provider sign off.", choices=choice_type_3, validators=[DataRequired()])
    # q_38 = RadioField(label="38.The EHR system has a built in alert system that prevents the prescriber from ordering medications that are documented in the system as an “allergy”.  ", choices=choice_type_3, validators=[DataRequired()])
    # q_39 = RadioField(label="39.The Physician is registered with the state prescription drug monitoring program and query the database according to state law.", choices=choice_type_3, validators=[DataRequired()])
    # q_40 = RadioField(label="40.Pain management plans of care are documented and reviewed with patients at each encounter.", choices=choice_type_3, validators=[DataRequired()])
    # q_41 = RadioField(label="41.If a patient is on high dose chronic opioid therapy, documentation in the chart reflects a plan to wean to a safe level or documentation reflects “why” the benefits of continued opioid therapy  outweighs the risks. ", choices=choice_type_3, validators=[DataRequired()])
    # q_42 = RadioField(label="42.My organization asks patients for feedback on their experience with an after visit survey.", choices=choice_type_3, validators=[DataRequired()])
    # q_43 = RadioField(label="43.My organization has a formal process to address patient complaints that includes notification and input from the physician involved in the patient's care.", choices=choice_type_3, validators=[DataRequired()])
    # q_44 = RadioField(label="44.I feel that my medical opinion and decision making ability is respected by my patients.", choices=choice_type_3, validators=[DataRequired()])
    # q_45 = RadioField(label="45.I have a wide variety of specialists within close geographic proximity that I can refer patients to with confidence.", choices=choice_type_3, validators=[DataRequired()])
    # q_46 = RadioField(label="46.I encounter barriers to specialty referral like geographical distance or insurance coverage.", choices=choice_type_3, validators=[DataRequired()])
    # q_47 = RadioField(label="47.I provide care via telemedicine.", choices=choice_type_3, validators=[DataRequired()])
    # q_48 = RadioField(label="48.There are challenges with telemedicine which prevent me from obtaining important information and not getting the whole clinical picture of the patient.", choices=choice_type_3, validators=[DataRequired()])
    # q_49 = RadioField(label="49.I'm aware of and stay updated on rules and regulations regarding telelmedine to ensure compliance.", choices=choice_type_3, validators=[DataRequired()])
    # q_50 = RadioField(label="50.After-hours calls and treatment advice is documented in the medical record. ", choices=choice_type_3, validators=[DataRequired()])
    # q_51 = RadioField(label="51.I review cross-coverage notes and advice given to my patients after hours.", choices=choice_type_3, validators=[DataRequired()])
    # q_52 = RadioField(label="52.Physician coverage for my organization is available 24 hours a day, 7 days a week.", choices=choice_type_3, validators=[DataRequired()])
    # q_53 = RadioField(label="53.A physician, advanced practice clinician or a licensed nurse answers all clinical questions and provides medical advice. ", choices=choice_type_3, validators=[DataRequired()])
    # q_54 = RadioField(label="54.Verbal and/or electronic communications with patients are documented in the medical record.", choices=choice_type_3, validators=[DataRequired()])
    # q_55 = RadioField(label="55.I have enough time in my schedule to perform a medical chart review before I enter the room to see my patient.", choices=choice_type_3, validators=[DataRequired()])
    # q_56 = RadioField(label="56.I have enough time in my schedule to evaluate and examine the patient to my satisfaction.", choices=choice_type_3, validators=[DataRequired()])
    # q_57 = RadioField(label="57.I have enough time in my schedule to educate and counsel the patient at the end of the encounter.", choices=choice_type_3, validators=[DataRequired()])
    # q_58 = RadioField(label="58.My medical staff does the education and counseling part of the visit.", choices=choice_type_3, validators=[DataRequired()])
    # q_59 = RadioField(label="59.I routinely have enough time in my schedule to complete chart documentation the same day of service.", choices=choice_type_3, validators=[DataRequired()])
    # q_60 = RadioField(label="60.I routinely have enough time in my schedule to complete chart documentation within a week of service.", choices=choice_type_3, validators=[DataRequired()])
    # q_61 = RadioField(label="61.I have sufficient time or a cross-coverage system to connect my patients with a live provider during office off-hours to assist with their care and treatment.", choices=choice_type_3, validators=[DataRequired()])
    # q_62 = RadioField(label="62.Orders and referrals are tracked to ensure all results are received in a timely manner.", choices=choice_type_3, validators=[DataRequired()])
    # q_63 = RadioField(label="63.Reports are run and reviewed to check for outstanding orders/results on a routine basis", choices=choice_type_3, validators=[DataRequired()])
    # q_64 = RadioField(label="64.Patients with outstanding results or referrals are contacted to determine follow through with recommended testing/referral.", choices=choice_type_3, validators=[DataRequired()])       
    # q_65 = RadioField(label="65.If patients are contacted about outstanding results or referrals, that communication is documented in the medical record.", choices=choice_type_3, validators=[DataRequired()])

    submit = SubmitField(label ="Submit")