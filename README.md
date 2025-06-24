# Content Creation Agency 🤖

An AI-powered agency designed to analyze trends, YouTube performance, and generate optimized content ideas and scripts. The agency leverages data-driven insights to create engaging content that fills identified market gaps in the AI and technology space.

## 🌟 Features

### 🤖 Multi-Agent Architecture
- **Content Manager**: Primary orchestrator that coordinates analysis and generates content ideas
- **Trend Analyzer**: Analyzes current AI trends and identifies content opportunities
- **YouTube Analyzer**: Analyzes channel performance, competitor content, and audience engagement

### 📊 Data-Driven Insights
- YouTube channel performance analysis
- Competitor content analysis
- Audience engagement metrics
- Trend analysis using web scraping and keyword analysis
- Sentiment analysis of video comments

### ✍️ Content Generation
- AI-powered content idea generation
- Detailed script creation in Markdown format
- Script editing and refinement capabilities
- Keyword extraction and analysis

### 🎯 Target Focus
- **Audience**: Technology enthusiasts, AI professionals, and learners
- **Content Focus**: AI, Machine Learning, and emerging technologies
- **Platform**: YouTube
- **Style**: Educational, informative, and engaging

## 🏗️ Architecture

The agency is built using the Agency Swarm framework, featuring three specialized agents:

```
Content Creation Agency
├── Content Manager (Orchestrator)
│   ├── ContentIdeaGenerator
│   ├── ScriptWriter
│   └── ScriptEditor
├── Trend Analyzer
│   ├── TavilySearchTool
│   ├── KeywordExtractor
│   └── TrendAnalyzer
└── YouTube Analyzer
    ├── ChannelAnalyzer
    ├── VideoPerformanceAnalyzer
    ├── CompetitorAnalyzer
    └── CommentAnalyzer
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Docker and Docker Compose (for deployment)
- API Keys:
  - OpenAI API Key
  - YouTube Data API Key
  - Tavily Search API Key

### Local Development Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd content-creation
   ```

2. **Set up environment variables**
   ```bash
   cp env.production.template .env
   # Edit .env with your actual API keys
   ```

3. **Install dependencies**
   ```bash
   pip install -r content_creation_agency/requirements.txt
   ```

4. **Run the agency**
   ```bash
   cd content_creation_agency
   python agency.py
   ```

### Docker Deployment

1. **Set up environment variables**
   ```bash
   cp env.production.template .env
   # Edit .env with your actual API keys
   ```

2. **Deploy using the provided script**
   ```bash
   chmod +x deploy.sh
   ./deploy.sh
   ```

3. **Or deploy manually with Docker Compose**
   ```bash
   docker-compose up --build -d
   ```

4. **Access the application**
   - Web Interface: http://localhost:7860
   - API Endpoints: Available through the Gradio interface

## 📋 API Keys Setup

### OpenAI API
1. Visit [OpenAI Platform](https://platform.openai.com/)
2. Create an account and generate an API key
3. Add to `.env`: `OPENAI_API_KEY=your_key_here`

### YouTube Data API
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a project and enable YouTube Data API v3
3. Create credentials (API Key)
4. Add to `.env`: `YOUTUBE_API_KEY=your_key_here`

### Tavily Search API
1. Visit [Tavily](https://tavily.com/)
2. Sign up and get your API key
3. Add to `.env`: `TAVILY_API_KEY=your_key_here`

## 🎮 Usage

### Web Interface
The agency provides a Gradio web interface for easy interaction:

1. Start the application (see deployment instructions above)
2. Open http://localhost:7860 in your browser
3. Use the interface to:
   - Analyze YouTube channels
   - Generate content ideas
   - Create and edit scripts
   - View trend analysis

### Programmatic Usage

```python
from content_creation_agency.agency import ContentCreationAgency

# Initialize the agency
agency = ContentCreationAgency()

# Analyze a YouTube channel
channel_analysis = agency.analyze_channel("UCSv4oL8vmoSH7GaPjuctRiC0")

# Generate content ideas
content_ideas = agency.generate_content_ideas()

# Create a script
script = agency.create_script(content_idea, target_length=10)
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | OpenAI API key for content generation | Yes |
| `YOUTUBE_API_KEY` | YouTube Data API key for channel analysis | Yes |
| `TAVILY_API_KEY` | Tavily Search API key for trend analysis | Yes |
| `GRADIO_SERVER_NAME` | Gradio server hostname | No |
| `GRADIO_SERVER_PORT` | Gradio server port | No |
| `LOG_LEVEL` | Logging level (INFO, DEBUG, etc.) | No |

### Customization

You can customize the agency by:
- Modifying agent instructions in `content_creation_agency/*/instructions.md`
- Adding new tools to agent tool folders
- Adjusting the agency manifesto in `content_creation_agency/agency_manifesto.md`

## 📁 Project Structure

```
content-creation/
├── content_creation_agency/
│   ├── content_manager/          # Content Manager agent
│   ├── trend_analyzer/           # Trend Analyzer agent
│   ├── youtube_analyzer/         # YouTube Analyzer agent
│   ├── agency.py                 # Main agency configuration
│   ├── agency_manifesto.md       # Shared agency instructions
│   ├── prd.txt                   # Product requirements document
│   └── requirements.txt          # Python dependencies
├── docker-compose.yml            # Docker Compose configuration
├── Dockerfile                    # Docker image definition
├── deploy.sh                     # Deployment script
├── env.production.template       # Environment variables template
└── README.md                     # This file
```

## 🧪 Testing

### Test Individual Tools
```bash
cd content_creation_agency
python -m pytest tests/
```

### Test the Agency
```bash
cd content_creation_agency
python agency.py
```

## 🚀 Production Deployment

### Using Render (Recommended)
1. Fork this repository
2. Connect to Render
3. Set environment variables in Render dashboard
4. Deploy automatically

### Using Docker
```bash
# Build and run
docker-compose up --build -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

### Using the Deployment Script
```bash
./deploy.sh
```

## 📊 Monitoring and Logs

- **Application Logs**: `logs/agency.log`
- **Docker Logs**: `docker-compose logs -f`
- **Health Check**: Available at http://localhost:7860/health

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- **Issues**: Create an issue on GitHub
- **Documentation**: Check the `PRODUCTION.md` file for detailed deployment information
- **Community**: Join our discussions in GitHub Discussions

## 🙏 Acknowledgments

- Built with [Agency Swarm](https://agency-swarm.ai/) framework
- Powered by OpenAI GPT models
- YouTube analysis via Google Data API
- Trend analysis via Tavily Search API

---

**Made with ❤️ for content creators** 