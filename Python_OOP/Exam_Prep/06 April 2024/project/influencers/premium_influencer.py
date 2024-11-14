from project.campaigns.base_campaign import BaseCampaign
from project.influencers.base_influencer import BaseInfluencer


class PremiumInfluencer(BaseInfluencer):
    PAYMENT = 0.85

    def calculate_payment(self, campaign: BaseCampaign) -> float:
        return float(campaign.budget * self.PAYMENT)

    def reached_followers(self, campaign_type: str) -> int:
        multiplier = 1.5 if campaign_type == 'HighBudgetCampaign' else 0.8

        return int(self.followers * self.engagement_rate * multiplier)

