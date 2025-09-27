import gradio as gr
import os
import logging
import tempfile
import shutil
from dotenv import load_dotenv

# Set up temporary directory for Agency Swarm settings
temp_dir = tempfile.mkdtemp()
os.environ['AGENCY_SWARM_SETTINGS_DIR'] = temp_dir

# Create a writable settings.json in temp directory
settings_path = os.path.join(temp_dir, 'settings.json')
os.makedirs(os.path.dirname(settings_path), exist_ok=True)

# Monkey patch the settings path to use temp directory
import agency_swarm.agents.agent as agent_module
original_save_settings = agent_module.Agent._save_settings

def patched_save_settings(self):
    """Patched version that uses temp directory"""
    try:
        # Use the temp directory for settings
        temp_settings_path = os.path.join(temp_dir, 'settings.json')
        with open(temp_settings_path, "w") as f:
            import json
            json.dump(self.settings, f, indent=2)
    except Exception as e:
        # If temp directory fails, try to create a minimal settings file
        pass

# Apply the patch
agent_module.Agent._save_settings = patched_save_settings

# Import agency after patching
from content_creation_agency.agency import agency

# Load environment variables
load_dotenv()

# Configure logging
log_file_path = os.path.join(temp_dir, 'agency.log')
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file_path),
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

def clear_chat():
    """Clear the chat history"""
    return None

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
        container=True
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
        outputs=[chatbot]
    )
    
    msg.submit(
        fn=process_request,
        inputs=[msg, chatbot],
        outputs=[chatbot]
    )
    
    clear_btn.click(clear_chat, None, chatbot, queue=False)

if __name__ == "__main__":
    # Get port from environment variable (Render provides this)
    port = int(os.environ.get("PORT", 7860))
    
    # Production settings
    demo.launch(
        server_name="0.0.0.0",  # Allow external connections
        server_port=port,       # Use Render's port
        share=False,            # Set to True for temporary public link
        debug=False,            # Disable debug mode in production
        show_error=True,        # Show errors to users
        quiet=False,            # Show startup messages
        inbrowser=False        # Don't open browser in production
    ) 