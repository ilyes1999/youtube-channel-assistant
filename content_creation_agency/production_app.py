import gradio as gr
import os
import logging
from dotenv import load_dotenv
from content_creation_agency.agency import agency

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('agency.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def process_request(user_input, history):
    """
    Process user input through the agency and return the response.
    """
    try:
        logger.info(f"Processing request: {user_input[:100]}...")
        
        # Use the agency's demo_gradio method for processing
        response = agency.demo_gradio(user_input, history)
        
        logger.info("Request processed successfully")
        return response
        
    except Exception as e:
        error_msg = f"Error processing request: {str(e)}"
        logger.error(error_msg)
        return error_msg

# Create the Gradio interface
with gr.Blocks(
    title="Content Creation Agency",
    theme=gr.themes.Soft(),
    css="""
    .gradio-container {
        max-width: 1200px !important;
        margin: auto !important;
    }
    """
) as demo:
    
    gr.Markdown("""
    # 🎬 Content Creation Agency
    
    **AI-Powered Content Creation & Analysis Platform**
    
    This agency helps you:
    - 📊 Analyze YouTube channel performance
    - 🔍 Research current AI trends
    - 💡 Generate content ideas
    - ✍️ Create and edit video scripts
    - 📈 Optimize content strategy
    
    ---
    """)
    
    chatbot = gr.Chatbot(
        height=600,
        show_label=False,
        container=True,
        bubble_full_width=False
    )
    
    with gr.Row():
        with gr.Column(scale=4):
            msg = gr.Textbox(
                placeholder="Ask me to analyze your channel, generate content ideas, or create scripts...",
                show_label=False,
                lines=2
            )
        
        with gr.Column(scale=1):
            submit_btn = gr.Button("Send", variant="primary", size="lg")
            clear_btn = gr.Button("Clear", variant="secondary")
    
    gr.Markdown("""
    ### Example Prompts:
    - "Analyze my YouTube channel performance"
    - "Generate 5 content ideas about AI trends"
    - "Create a script about machine learning basics"
    - "Research current AI trends for content"
    """)
    
    # Event handlers
    submit_btn.click(
        fn=process_request,
        inputs=[msg, chatbot],
        outputs=[chatbot],
        clear_input=True
    )
    
    msg.submit(
        fn=process_request,
        inputs=[msg, chatbot],
        outputs=[chatbot],
        clear_input=True
    )
    
    clear_btn.click(lambda: None, None, chatbot, queue=False)

if __name__ == "__main__":
    # Production settings
    demo.launch(
        server_name="0.0.0.0",  # Allow external connections
        server_port=7860,       # Default Gradio port
        share=False,            # Set to True for temporary public link
        debug=False,            # Disable debug mode in production
        show_error=True,        # Show errors to users
        quiet=False,            # Show startup messages
        inbrowser=True          # Open browser automatically
    ) 