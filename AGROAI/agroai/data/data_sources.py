import random
import json
from datetime import datetime, timedelta

class OceanDataProcessor:
    def __init__(self):
        self.regions = ['Pacific', 'Atlantic', 'Indian', 'Arctic', 'Southern', 'Mediterranean']
        self.parameters = ['temperature', 'salinity', 'ph', 'dissolved_oxygen', 'chlorophyll', 'turbidity']
        self.marine_species = ['phytoplankton', 'zooplankton', 'coral', 'fish', 'marine_mammals', 'seaweed']

    def analyze_query(self, query):
        query_lower = query.lower()
        
        # Simulate data analysis based on query
        if any(word in query_lower for word in ['temperature', 'temp', 'thermal']):
            return self._analyze_temperature_data(query)
        elif any(word in query_lower for word in ['salinity', 'salt']):
            return self._analyze_salinity_data(query)
        elif any(word in query_lower for word in ['ph', 'acidity']):
            return self._analyze_ph_data(query)
        elif any(word in query_lower for word in ['oxygen', 'o2']):
            return self._analyze_oxygen_data(query)
        elif any(word in query_lower for word in ['ecosystem', 'marine', 'species']):
            return self._analyze_ecosystem_data(query)
        else:
            return self._generate_general_analysis(query)

    def _analyze_temperature_data(self, query):
        data = {
            'current_temp': round(random.uniform(15, 30), 2),
            'trend': random.choice(['increasing', 'decreasing', 'stable']),
            'anomaly': round(random.uniform(-2, 2), 2),
            'region': random.choice(self.regions)
        }
        
        return {
            'has_data': True,
            'insights': f"- Sea surface temperature: {data['current_temp']}°C\n- Trend: {data['trend']}\n- Temperature anomaly: {data['anomaly']}°C\n- Region: {data['region']} Ocean",
            'summary': f"Temperature analysis shows {data['trend']} trend with {data['anomaly']}°C anomaly in {data['region']} Ocean.",
            'recommendations': "Monitor seasonal variations, check for coral bleaching alerts, analyze thermal stress patterns.",
            'data': data
        }

    def _analyze_salinity_data(self, query):
        data = {
            'salinity': round(random.uniform(30, 40), 2),
            'variation': round(random.uniform(0.5, 5), 2),
            'freshwater_influence': random.choice(['low', 'moderate', 'high']),
            'region': random.choice(self.regions)
        }
        
        return {
            'has_data': True,
            'insights': f"- Salinity level: {data['salinity']} PSU\n- Seasonal variation: {data['variation']} PSU\n- Freshwater influence: {data['freshwater_influence']}\n- Region: {data['region']} Ocean",
            'summary': f"Salinity patterns show {data['freshwater_influence']} freshwater influence in {data['region']} Ocean.",
            'recommendations': "Analyze evaporation-precipitation balance, monitor river discharge impacts, study density currents.",
            'data': data
        }

    def _analyze_ph_data(self, query):
        data = {
            'ph': round(random.uniform(7.8, 8.3), 2),
            'acidification_trend': round(random.uniform(-0.02, 0), 3),
            'carbonate_saturation': random.choice(['adequate', 'marginal', 'low']),
            'region': random.choice(self.regions)
        }
        
        return {
            'has_data': True,
            'insights': f"- pH level: {data['ph']}\n- Acidification trend: {data['acidification_trend']} per decade\n- Carbonate saturation: {data['carbonate_saturation']}\n- Region: {data['region']} Ocean",
            'summary': f"Ocean acidification monitoring shows {data['acidification_trend']} pH change per decade in {data['region']} Ocean.",
            'recommendations': "Monitor carbonate chemistry, assess impacts on calcifying organisms, study CO2 absorption patterns.",
            'data': data
        }

    def _analyze_oxygen_data(self, query):
        data = {
            'oxygen': round(random.uniform(4, 9), 2),
            'hypoxic_zones': random.randint(0, 5),
            'seasonal_variation': round(random.uniform(0.5, 2), 2),
            'region': random.choice(self.regions)
        }
        
        return {
            'has_data': True,
            'insights': f"- Dissolved oxygen: {data['oxygen']} mg/L\n- Hypoxic zones detected: {data['hypoxic_zones']}\n- Seasonal variation: {data['seasonal_variation']} mg/L\n- Region: {data['region']} Ocean",
            'summary': f"Oxygen levels show {data['hypoxic_zones']} hypoxic zones in {data['region']} Ocean with seasonal variation of {data['seasonal_variation']} mg/L.",
            'recommendations': "Monitor oxygen minimum zones, study stratification effects, assess impacts on marine life.",
            'data': data
        }

    def _analyze_ecosystem_data(self, query):
        data = {
            'biodiversity_index': round(random.uniform(0.6, 0.95), 3),
            'primary_production': round(random.uniform(100, 500), 2),
            'key_species': random.sample(self.marine_species, 3),
            'ecosystem_health': random.choice(['excellent', 'good', 'fair', 'poor']),
            'region': random.choice(self.regions)
        }
        
        return {
            'has_data': True,
            'insights': f"- Biodiversity index: {data['biodiversity_index']}\n- Primary production: {data['primary_production']} mg C/m²/day\n- Key species: {', '.join(data['key_species'])}\n- Ecosystem health: {data['ecosystem_health']}\n- Region: {data['region']} Ocean",
            'summary': f"Marine ecosystem assessment shows {data['ecosystem_health']} health with biodiversity index of {data['biodiversity_index']} in {data['region']} Ocean.",
            'recommendations': "Monitor species distribution, assess habitat quality, study food web dynamics, track conservation status.",
            'data': data
        }

    def _generate_general_analysis(self, query):
        return {
            'has_data': False,
            'insights': "This appears to be a general oceanographic inquiry. I can provide insights on various ocean parameters and marine ecosystems.",
            'summary': "General ocean data analysis capabilities available for multiple parameters and regions.",
            'recommendations': "Consider specifying ocean parameters (temperature, salinity, pH, oxygen) or marine ecosystem aspects for detailed analysis."
        }

    def generate_visualization_data(self, query):
        # Generate sample data for visualization
        time_points = 12
        base_date = datetime.now() - timedelta(days=365)
        
        chart_data = {}
        for param in random.sample(self.parameters, 3):
            chart_data[param] = [
                {
                    'date': (base_date + timedelta(days=i*30)).strftime('%Y-%m-%d'),
                    'value': round(random.uniform(10, 35) if param == 'temperature' else 
                                  random.uniform(30, 40) if param == 'salinity' else
                                  random.uniform(7.8, 8.3) if param == 'ph' else
                                  random.uniform(4, 9) if param == 'dissolved_oxygen' else
                                  random.uniform(0.1, 5) if param == 'chlorophyll' else
                                  random.uniform(1, 10), 2)
                }
                for i in range(time_points)
            ]
        
        return {
            'chart_type': 'Time Series Analysis',
            'data_points': time_points,
            'time_range': '12 months',
            'parameters': list(chart_data.keys()),
            'data': chart_data,
            'description': f"trends in {', '.join(list(chart_data.keys()))} over the past year"
        }