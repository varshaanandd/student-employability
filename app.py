import gradio as gr
import pandas as pd

# Function to assess employability
def assess_employability(name, email, communication, problem_solving, teamwork, adaptability, appearance, speaking, alertness, presentation):
    score = (communication + problem_solving + teamwork + adaptability + appearance + speaking + alertness + presentation) / 8
    
    if score >= 7:
        message = f" {name}, you're highly employable! Keep pushing forward! 🚀"
    elif score >= 5:
        message = f" {name}, you have potential! Work on improving and you'll be there soon! ✨"
    else:
        message = f" {name}, you might need to enhance your skills. Keep learning and improving! 📚"
    
    return message

# Gradio UI
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("##  **Employability Skill Checker** ")
    gr.Markdown("### Drag the sliders to rate your skills!")

    name = gr.Textbox(label="Enter Your Name", placeholder="Type your name here...")
    email = gr.Textbox(label="Enter Your Email", placeholder="Type your email here...")
    
    communication = gr.Slider(1, 10, label=" Communication Skills")
    problem_solving = gr.Slider(1, 10, label=" Problem-Solving Skills")
    teamwork = gr.Slider(1, 10, label=" Teamwork Ability")
    adaptability = gr.Slider(1, 10, label=" Adaptability to Changes")
    appearance = gr.Slider(1, 10, label=" General Appearance")
    speaking = gr.Slider(1, 10, label="Manner of Speaking")
    alertness = gr.Slider(1, 10, label=" Mental Alertness")
    presentation = gr.Slider(1, 10, label=" Ability to Present Ideas")
  
    submit_btn = gr.Button(" Check Employability ")
    output = gr.Textbox(label="Result", interactive=False)

    submit_btn.click(assess_employability, inputs=[name, email, communication, problem_solving, teamwork, adaptability, appearance, speaking, alertness, presentation], outputs=output)

# Launch the app
if __name__ == "__main__":
    demo.launch()

