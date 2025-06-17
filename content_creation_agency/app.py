import gradio as gr
from content_creation_agency.agency import process_single_message
import os
from dotenv import load_dotenv

load_dotenv()

def process_request(user_input):
    """
    Process user input through the agency and return the response.
    """
    try:
        # Use the new process_single_message method
        response = process_single_message(user_input)
        return response
    except Exception as e:
        return f"Error: {str(e)}"

# Create the Gradio interface
with gr.Blocks(title="Content Creation Agency") as demo:
    gr.Markdown("""
    # Content Creation Agency
    This interface allows you to interact with the Content Creation Agency to:
    - Generate content ideas
    - Analyze trends
    - Create and edit scripts
    - Analyze YouTube performance
    """)
    
    with gr.Row():
        with gr.Column():
            user_input = gr.Textbox(
                label="Your Request",
                placeholder="Enter your request here...",
                lines=5
            )
            submit_btn = gr.Button("Submit")
        
        with gr.Column():
            output = gr.Textbox(
                label="Agency Response",
                lines=10,
                interactive=False
            )
    
    submit_btn.click(
        fn=process_request,
        inputs=user_input,
        outputs=output
    )

if __name__ == "__main__":
    demo.launch() 