import gradio as gr

# Function to check employability
def check_employability(name, communication, problem_solving, time_management, networking, teamwork):
    score = (communication + problem_solving + time_management + networking + teamwork) / 5

    if score >= 7:
        message = f"🚀 {name}, you are highly employable! Keep it up! 🚀"
    elif score >= 5:
        message = f"✨ {name}, you have potential! Keep improving! ✨"
    else:
        message = f"😟 {name}, work on your skills! Keep learning! 📚"

    return message

# Gradio UI - Card Style Layout
with gr.Blocks(theme=gr.themes.Base()) as app:
    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("<h3 style='text-align: center; color: #2E86C1;'>📊 Employability Check</h3>")
            gr.Markdown("Rate your skills from 1 to 10 to get an employability prediction!")
        
    with gr.Row():
        with gr.Column(scale=1, min_width=400):  # Compact card-style UI
            name = gr.Textbox(label="Your Name", placeholder="Enter your name", interactive=True)
            
            gr.Markdown("#### 🎯 Rate Your Skills (1-10)")
            communication = gr.Slider(1, 10, label="💬 Communication", value=5, interactive=True)
            problem_solving = gr.Slider(1, 10, label="🧐 Problem Solving", value=5, interactive=True)
            time_management = gr.Slider(1, 10, label="⏳ Time Management", value=5, interactive=True)
            networking = gr.Slider(1, 10, label="👥 Networking", value=5, interactive=True)
            teamwork = gr.Slider(1, 10, label="🤝 Teamwork", value=5, interactive=True)
            
            button = gr.Button("🚀 Check Employability 🚀")
            result = gr.Textbox(label="Employability Status", interactive=False)
            
            button.click(check_employability, inputs=[name, communication, problem_solving, time_management, networking, teamwork], outputs=result)

# Start the app
if __name__ == "__main__":
    app.launch()
