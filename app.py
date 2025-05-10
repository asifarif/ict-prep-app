# app.py
import gradio as gr
from api import call_groq_api

TOPICS = [
    "Computer Hardware Basics", "Operating Systems", "Software Development Lifecycle",
    "Networking Fundamentals", "Internet Protocols", "Cybersecurity Basics",
    "Cloud Computing", "Database Management", "Web Development", "Mobile Computing",
    "Data Structures", "Algorithms", "Artificial Intelligence", "Machine Learning",
    "Internet of Things (IoT)", "Ethical Issues in ICT"
]

def generate_question(topic, bloom_level):
    prompt = f"Generate a short {bloom_level} level exam question for {topic} and dont show the answer with the question."
    return call_groq_api(prompt)

def evaluate_answer(question, answer):
    prompt = f"Evaluate this answer:\nQ: {question}\nA: {answer}\nGive a score out of 10 and brief feedback."
    return call_groq_api(prompt)

def exam_bot(topic, bloom_level, generate_btn, submit_btn, answer, state=None):
    if state is None:
        state = {"question": None, "score": "", "feedback": ""}

    if generate_btn and topic and bloom_level:
        question = generate_question(topic, bloom_level)
        state["question"] = question
        state["score"] = ""
        state["feedback"] = ""
        return question, "", "", "", state

    if submit_btn and state["question"] and answer:
        result = evaluate_answer(state["question"], answer)
        # Extract score and feedback (assuming format: "Score: X/10\nFeedback: ...")
        lines = result.split("\n")
        score = next((line for line in lines if "Score:" in line), "")
        feedback = next((line for line in lines if "Feedback:" in line), "")
        state["score"] = score if score else ""
        state["feedback"] = feedback if feedback else ""
        return state["question"], score, feedback, answer, state

    return state.get("question", ""), state["score"], state["feedback"], answer, state

with gr.Blocks() as app:
    gr.Markdown("## 🎓 Applications of ICT Exam Prep Chatbot")
    with gr.Row():
        with gr.Column():
            topic_dropdown = gr.Dropdown(choices=TOPICS, label="Select Topic", value=TOPICS[0])
            bloom_radio = gr.Radio(choices=["C2 (Understanding)", "C3 (Applying)"], label="Bloom’s Level", value="C2 (Understanding)")
            generate_btn = gr.Button("Generate Question")
        with gr.Column():
            question_box = gr.Textbox(label="Question", interactive=False, lines=3)
            answer_box = gr.Textbox(label="Your Answer", lines=4, placeholder="Type your answer here...")
            submit_btn = gr.Button("Submit Answer")
    with gr.Row():
        with gr.Column():
            score_box = gr.Textbox(label="Score", interactive=False)
            feedback_box = gr.Textbox(label="Feedback", interactive=False, lines=4)
    state = gr.State()

    generate_btn.click(
        exam_bot,
        inputs=[topic_dropdown, bloom_radio, gr.State(value=True), gr.State(value=False), gr.State(value=""), state],
        outputs=[question_box, score_box, feedback_box, answer_box, state]
    )
    submit_btn.click(
        exam_bot,
        inputs=[topic_dropdown, bloom_radio, gr.State(value=False), gr.State(value=True), answer_box, state],
        outputs=[question_box, score_box, feedback_box, answer_box, state]
    )

if __name__ == "__main__":
    app.launch()