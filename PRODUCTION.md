# Production Deployment Guide

## 🚀 Quick Start

### Option 1: Local Production (Recommended for testing)

1. **Install dependencies:**
   ```bash
   pip install -r content_creation_agency/requirements.txt
   pip install -e .
   ```

2. **Set up environment variables:**
   ```bash
   # Create .env file with your API keys
   cp env.production.template .env
   # Edit .env with your actual API keys
   ```

3. **Run the production app:**
   ```bash
   python content_creation_agency/production_app.py
   ```

4. **Access the application:**
   - Open http://localhost:7860 in your browser

### Option 2: Docker Deployment

1. **Set up environment variables:**
   ```bash
   cp env.production.template .env
   # Edit .env with your actual API keys
   ```

2. **Deploy with Docker Compose:**
   ```bash
   chmod +x deploy.sh
   ./deploy.sh
   ```

3. **Or manually:**
   ```bash
   docker-compose up --build -d
   ```

### Option 3: Cloud Deployment

#### Render.com
1. Connect your GitHub repository to Render
2. Create a new Web Service
3. Use the `render.yaml` configuration
4. Set environment variables in Render dashboard

#### Railway.app
1. Connect your GitHub repository to Railway
2. Railway will auto-detect the Python app
3. Set environment variables in Railway dashboard
4. Deploy automatically

#### Heroku
1. Install Heroku CLI
2. Create a new Heroku app
3. Set environment variables:
   ```bash
   heroku config:set OPENAI_API_KEY=your_key
   heroku config:set YOUTUBE_API_KEY=your_key
   heroku config:set TAVILY_API_KEY=your_key
   ```
4. Deploy:
   ```bash
   git push heroku main
   ```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | OpenAI API key for GPT models | Yes |
| `YOUTUBE_API_KEY` | YouTube Data API key | Yes |
| `TAVILY_API_KEY` | Tavily search API key | Yes |
| `GRADIO_SERVER_NAME` | Server hostname (default: 0.0.0.0) | No |
| `GRADIO_SERVER_PORT` | Server port (default: 7860) | No |

### API Keys Setup

1. **OpenAI API Key:**
   - Visit https://platform.openai.com/api-keys
   - Create a new API key
   - Add to your environment variables

2. **YouTube Data API Key:**
   - Visit https://console.cloud.google.com/
   - Enable YouTube Data API v3
   - Create credentials (API key)
   - Add to your environment variables

3. **Tavily API Key:**
   - Visit https://tavily.com/
   - Sign up and get your API key
   - Add to your environment variables

## 📊 Monitoring & Logging

### Logs
- Application logs: `logs/agency.log`
- Docker logs: `docker-compose logs -f`
- System logs: Check your deployment platform's logging

### Health Checks
- Endpoint: `http://your-domain/`
- Docker health check runs every 30 seconds
- Application responds with 200 OK when healthy

## 🔒 Security Considerations

1. **API Keys:**
   - Never commit API keys to version control
   - Use environment variables for all secrets
   - Rotate keys regularly

2. **Network Security:**
   - Use HTTPS in production
   - Configure CORS properly
   - Limit access to trusted domains

3. **Rate Limiting:**
   - Implement rate limiting for API endpoints
   - Monitor API usage to prevent abuse

## 🚀 Scaling

### Horizontal Scaling
- Use load balancers for multiple instances
- Implement session management
- Use external databases for state

### Vertical Scaling
- Increase CPU/memory allocation
- Optimize model usage
- Cache frequently used data

## 🛠️ Troubleshooting

### Common Issues

1. **API Key Errors:**
   - Verify all API keys are set correctly
   - Check API key permissions and quotas
   - Ensure keys are valid and active

2. **Port Conflicts:**
   - Change `GRADIO_SERVER_PORT` if 7860 is in use
   - Check firewall settings

3. **Memory Issues:**
   - Increase container memory limits
   - Optimize model loading
   - Implement caching

### Debug Mode
Enable debug mode for troubleshooting:
```bash
export GRADIO_DEBUG=true
python content_creation_agency/production_app.py
```

## 📈 Performance Optimization

1. **Model Optimization:**
   - Use smaller models for faster responses
   - Implement response caching
   - Batch similar requests

2. **Infrastructure:**
   - Use CDN for static assets
   - Implement database connection pooling
   - Use async processing for long tasks

3. **Monitoring:**
   - Set up application performance monitoring
   - Monitor API response times
   - Track error rates and user metrics

## 🔄 Updates & Maintenance

### Updating the Application
1. Pull latest changes: `git pull origin main`
2. Update dependencies: `pip install -r requirements.txt`
3. Restart the application
4. Test functionality

### Backup Strategy
- Backup environment variables
- Export any persistent data
- Document configuration changes

## 📞 Support

For issues and questions:
1. Check the logs for error messages
2. Review this documentation
3. Check the Agency Swarm documentation
4. Create an issue in the repository 