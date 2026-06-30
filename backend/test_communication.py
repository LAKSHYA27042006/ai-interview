from services.communication_analysis_service import CommunicationAnalysisService

service = CommunicationAnalysisService()

result = service.analyze(
    "../dataset/processed/interview_01/transcript/transcript.json"
)

print("\n========== COMMUNICATION ANALYSIS ==========\n")

for key, value in result.items():
    print(f"{key} : {value}")