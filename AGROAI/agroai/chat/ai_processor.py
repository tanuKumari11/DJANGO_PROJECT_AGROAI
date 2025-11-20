import re
import json
import random
from datetime import datetime
from data.data_sources import OceanDataProcessor

class AgroAIProcessor:
    def __init__(self):
        self.ocean_processor = OceanDataProcessor()
        self.greeting_patterns = [
            "hi", "hello", "hey", "good morning", "good afternoon", "good evening"
        ]
        self.ocean_keywords = [
            'temperature', 'salinity', 'ph', 'oxygen', 'current', 'wave', 
            'tide', 'marine', 'ocean', 'sea', 'coastal', 'fishery',
            'aquaculture', 'algae', 'plankton', 'coral', 'ecosystem'
        ]

    def process_message(self, message, conversation):
        message_lower = message.lower()
        
        # Check for greetings
        if any(greeting in message_lower for greeting in self.greeting_patterns):
            return self._generate_greeting_response()
        
        # Check for ocean data queries
        if any(keyword in message_lower for keyword in self.ocean_keywords):
            return self._process_ocean_query(message, conversation)
        
        # Check for data visualization requests
        if any(word in message_lower for word in ['graph', 'chart', 'plot', 'visualize', 'show data']):
            return self._generate_visualization(message)
        
        # Default response
        return self._generate_general_response(message)

    def _generate_greeting_response(self):
        greetings = [
            "Hello! I'm AgroAI, your ocean data assistant. How can I help you with ocean research today?",
            "Hi there! Ready to explore ocean data and marine insights?",
            "Welcome to AgroAI! I specialize in ocean data analysis and marine ecosystem research."
        ]
        return {
            'content': random.choice(greetings),
            'type': 'text'
        }

    def _process_ocean_query(self, message, conversation):
        # Analyze the query and provide relevant ocean data
        analysis = self.ocean_processor.analyze_query(message)
        
        if analysis['has_data']:
            response_content = f"""
🌊 **Ocean Data Analysis**

**Query:** {message}

**Key Insights:**
{analysis['insights']}

**Data Summary:**
{analysis['summary']}

**Recommended Actions:**
{analysis['recommendations']}

*Data processed using AgroAI Ocean Intelligence*
            """
        else:
            response_content = f"""
🔍 **Ocean Research Assistant**

I've analyzed your query about: **{message}**

While I don't have specific data for this exact request, here's what I can tell you about ocean monitoring:

**General Ocean Parameters:**
- Temperature: 15-30°C (varies by region and depth)
- Salinity: 30-40 PSU (Practical Salinity Units)
- pH: 7.8-8.3 (slightly alkaline)
- Dissolved Oxygen: 4-9 mg/L

**Suggested Analysis:**
1. Check regional oceanographic data
2. Analyze seasonal variations
3. Monitor ecosystem health indicators
4. Compare with historical trends

Would you like me to generate sample data visualization for ocean parameters?
            """
        
        return {
            'content': response_content,
            'type': 'data_analysis',
            'data': analysis.get('data', {})
        }

    def _generate_visualization(self, message):
        # Generate visualization data
        viz_data = self.ocean_processor.generate_visualization_data(message)
        
        response_content = f"""
📊 **Ocean Data Visualization**

**Generated Chart:** {viz_data['chart_type']}

**Parameters:**
- Data Points: {viz_data['data_points']}
- Time Range: {viz_data['time_range']}
- Parameters Measured: {', '.join(viz_data['parameters'])}

**Visualization Ready!** The chart has been generated showing {viz_data['description']}.

*Tip: You can ask for specific parameters like temperature trends, salinity distribution, or ecosystem metrics.*
        """
        
        return {
            'content': response_content,
            'type': 'visualization',
            'visualization_data': viz_data
        }

    def _generate_general_response(self, message):
        responses = [
            f"I understand you're asking about: '{message}'. As an ocean data specialist, I can help you analyze marine ecosystems, ocean parameters, and environmental data.",
            f"Interesting question about '{message}'. Let me connect this to ocean research context. I can assist with data analysis, trend identification, and marine ecosystem insights.",
            f"Regarding '{message}', I can provide ocean-related insights and data analysis. Would you like me to search for specific marine data or generate ocean parameter visualizations?"
        ]
        
        return {
            'content': random.choice(responses),
            'type': 'text'
        }