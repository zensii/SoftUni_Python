from typing import List, Dict

from project.campaigns.base_campaign import BaseCampaign
from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.influencers.base_influencer import BaseInfluencer
from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.standard_influencer import StandardInfluencer


class InfluencerManagerApp:

    def __init__(self):
        self.influencers: List[BaseInfluencer] = []
        self.campaigns: List[BaseCampaign] = []

    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float) -> str:

        influencer_t = {"PremiumInfluencer": PremiumInfluencer, "StandardInfluencer": StandardInfluencer}.get(influencer_type, None)

        if influencer_t is None:
            return f"{influencer_type} is not an allowed influencer type."
        if username in [i.username for i in self.influencers]:
            return f"{username} is already registered."

        influencer = influencer_t(username, followers, engagement_rate)
        self.influencers.append(influencer)
        return f"{username} is successfully registered as a {influencer_type}."


    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float) -> str:

        camp_t = {"HighBudgetCampaign": HighBudgetCampaign, "LowBudgetCampaign": LowBudgetCampaign}.get(campaign_type, None)

        if camp_t is None:
            return f"{campaign_type} is not a valid campaign type."
        if campaign_id in [c.campaign_id for c in self.campaigns]:
            return f"Campaign ID {campaign_id} has already been created."

        campaign = camp_t(campaign_id, brand, required_engagement)
        self.campaigns.append(campaign)
        return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."


    def participate_in_campaign(self, influencer_username: str, campaign_id: int) -> str:

        if not influencer_username in [i.username for i in self.influencers]:
            return f"Influencer '{influencer_username}' not found."

        if not campaign_id in [c.campaign_id for c in self.campaigns]:
            return f"Campaign with ID {campaign_id} not found."

        influencer = [i for i in self.influencers if i.username == influencer_username][0]
        campaign = [c for c in self.campaigns if c.campaign_id == campaign_id][0]

        if not campaign.check_eligibility(influencer.engagement_rate):
            return f"Influencer '{influencer_username}' does not meet the eligibility criteria for the campaign with ID {campaign_id}."

        money_earned = influencer.calculate_payment(campaign)

        if money_earned > 0.0:
            campaign.approved_influencers.append(influencer)
            campaign.budget -= money_earned
            influencer.campaigns_participated.append(campaign)
            return f"Influencer '{influencer_username}' has successfully participated in the campaign with ID {campaign_id}."

    def calculate_total_reached_followers(self) -> Dict[BaseCampaign, int]:
        result = {}

        for campaign in sorted(self.campaigns, key= lambda c: (len(c.approved_influencers), -c.budget)):
            total_followers = 0
            influencers = campaign.approved_influencers
            if influencers:
                for influencer in influencers:
                    total_followers += influencer.reached_followers(campaign.__class__.__name__)
                result[campaign] = total_followers
        return result


    def influencer_campaign_report(self, username: str):
        influencer = [i for i in self.influencers if i.username == username][0]

        return influencer.display_campaigns_participated()


    def campaign_statistics(self):

        # self.campaigns.sort(key= lambda c: (len(c.approved_influencers), -c.budget))   # should i sort the actual list or just sort for the printing?! to check

        result = "$$ Campaign Statistics $$"
        for campaign, total_followers in self.calculate_total_reached_followers().items():
            result += (f"\n  * Brand: {campaign.brand}, Total influencers: {len(campaign.approved_influencers)},"
                       f" Total budget: ${campaign.budget:.2f}, Total reached followers: {total_followers}")
        return result
