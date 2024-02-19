import streamlit as st
import pickle
import numpy as np

# Load the model from the file
with open("model.pkl", "rb") as f:
    mental = pickle.load(f)

st.set_page_config("MindSight ",page_icon=":brain:")

def multiple_choice_question(question, options):
    st.write(question)
    option = st.radio(f"Choose an option for ", options, key=question)
    return option

def display_prevention_info(predicted_disease):
    # st.subheader("Prevention of Predicted Disease")
    if predicted_disease == "Bipolar Type-1":
        st.write("Bipolar disorder type I is a serious mental illness. While it cannot be prevented entirely, there are ways to manage and reduce the risk of episodes:")         
        st.subheader("Causes of Bipolar Type-1:")
        st.write("- Genetic factors")
        st.write("- Chemical imbalances in the brain")
        st.write("- Environmental factors")
        
        st.subheader("Prevention and Management Tips:")
        st.write("- Seek regular medical care and attend therapy sessions.")
        st.write("- Maintain a stable routine and get enough sleep.")
        st.write("- Avoid drugs and alcohol, as they can trigger episodes.")
        st.write("- Learn to recognize the warning signs of an episode and have a plan in place to manage them.")
        st.write("- Build a strong support system with friends, family, and mental health professionals.")

    elif predicted_disease == "Bipolar Type-2":
        st.write("Bipolar disorder type II involves periods of depression alternating with hypomania, a less severe form of mania. Prevention strategies include:")
        
        st.subheader("Causes of Bipolar Type-2:")
        st.write("- Genetic predisposition")
        st.write("- Biological differences in brain chemistry")
        st.write("- Environmental factors")
        
        st.subheader("Prevention and Management Tips:")
        st.write("- Regular monitoring and treatment under the guidance of mental health professionals.")
        st.write("- Develop coping strategies and stress management techniques.")
        st.write("- Maintain a healthy lifestyle with adequate sleep, nutrition, and exercise.")

    elif predicted_disease == "Depression":
        st.write("Depression is a common mental health disorder characterized by persistent feelings of sadness and loss of interest or pleasure in activities. Prevention and management strategies include:")
       
        st.subheader("Causes of Depression:")
        st.write("- Genetics")
        st.write("- Brain chemistry and structure")
        st.write("- Life events and situations")
        
        st.subheader("Prevention and Management Tips:")
        st.write("- Seek professional help and therapy.")
        st.write("- Engage in regular physical activity and exercise.")
        st.write("- Maintain a healthy diet and lifestyle.")
        st.write("- Practice stress reduction techniques such as mindfulness and relaxation exercises.")

    else:
        st.write("It seems like you are doing well! Remember to prioritize your mental health by practicing self-care, seeking support from loved ones, and engaging in activities that bring you joy and fulfillment.")

def main():
    st.title("MindSight")
    
    st.write("Welcome to our Mental Health Disorder Detection Model")
    st.write("Check your mental health with the help of our application")
    st.write("Please answer the following questions to get started.")
  
    questions = [
        "Do you often feel exhausted?",
        "Do you experience mood swings?",
        "Do you ever have thoughts of harming yourself or ending your life?",
        "Do you often respond aggressively when upset or frustrated?",
        "Do you often just let things go when they bother you?",
        "Do you often feel like you're going to have a nervous breakdown?",
        "Do you find it easy to admit when you've made a mistake?",
        "Do you avoid eating?",
        "Do you usually sleep well at night?",
    ]

    options = [
        ["Sometimes", "Usually", "Seldom", "Most-Often"],
        ["YES", "NO"],
        ["YES", "NO"],
        ["YES", "NO"],
        ["YES", "NO"],
        ["YES", "NO"],
        ["YES", "NO"],
        ["YES", "NO"],
        ["YES", "NO"],
    ]

    option_to_value = {
        "Sometimes": 2,
        "Usually": 3,
        "Seldom": 1,
        "Most-Often": 0,
        "YES": 1,
        "NO": 0,
    }

    features = []
    for i in range(len(questions)):
        user_answer = multiple_choice_question(questions[i], options[i])
        numerical_answer = option_to_value[user_answer]
        features.append(numerical_answer)

    sadness = st.slider("How would you rate your current level of sadness? (1 being not sad at all and 10 being extremely sad?", 1, 10)
    concentration = st.slider("What is your Concentration level?", 1, 10)
    overthinking = st.slider("How often you overthink", 1, 10)
    features.extend([sadness, concentration, overthinking])
    features = np.array(features).reshape(1, -1)
    labels = ["Bipolar Type-1", "Bipolar Type-2", "Depression", "Normal"]
    
    if st.button("Predict"):  # Add a button for prediction
        prediction = mental.predict(features)
        predicted_label = labels[int(prediction)]
        st.markdown(f"Your Mental Condition: **{predicted_label}**")
        
        display_prevention_info(predicted_label)

if __name__ == "__main__":
    main()
