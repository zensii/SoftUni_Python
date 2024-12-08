from typing import List

from project.artifacts.base_artifact import BaseArtifact
from project.artifacts.contemporary_artifact import ContemporaryArtifact
from project.artifacts.renaissance_artifact import RenaissanceArtifact
from project.collectors.base_collector import BaseCollector
from project.collectors.museum import Museum
from project.collectors.private_collector import PrivateCollector


class AuctionHouseManagerApp:

    ARTIFACT_TYPES = {"RenaissanceArtifact": RenaissanceArtifact, "ContemporaryArtifact": ContemporaryArtifact}
    COLLECTOR_TYPES = {"Museum": Museum, "PrivateCollector": PrivateCollector}

    def __init__(self):
        self.artifacts: List[BaseArtifact] = []
        self.collectors: List[BaseCollector] = []

    def register_artifact(self, artifact_type: str, artifact_name: str, artifact_price: float, artifact_space: int):
        if artifact_type not in self.ARTIFACT_TYPES:
            raise ValueError("Unknown artifact type!")
        if [a for a in self.artifacts if a.name == artifact_name]:
            raise ValueError(f"{artifact_name} has been already registered!")
        new_artifact = self.ARTIFACT_TYPES[artifact_type](artifact_name, artifact_price, artifact_space)
        self.artifacts.append(new_artifact)
        return f"{artifact_name} is successfully added to the auction as {artifact_type}."

    def register_collector(self, collector_type: str, collector_name: str):
        if collector_type not in self.COLLECTOR_TYPES:
            raise ValueError("Unknown collector type!")
        if [c for c in self.collectors if c.name == collector_name]:
            raise ValueError(f"{collector_name} has been already registered!")
        new_collector = self.COLLECTOR_TYPES[collector_type](collector_name)
        self.collectors.append(new_collector)
        return f"{collector_name} is successfully registered as a {collector_type}."

    def perform_purchase(self, collector_name: str, artifact_name: str):
        collector = [c for c in self.collectors if c.name == collector_name]
        artifact = [a for a in self.artifacts if a.name == artifact_name]

        if not collector:
            raise ValueError(f"Collector {collector_name} is not registered to the auction!")
        collector = collector[0]
        if not artifact:
            raise ValueError(f"Artifact {artifact_name} is not registered to the auction!")
        artifact = artifact[0]
        if not collector.can_purchase(artifact.price, artifact.space_required):
            return "Purchase is impossible."

        self.artifacts.remove(artifact)
        collector.purchased_artifacts.append(artifact)
        collector.available_money -= artifact.price
        collector.available_space -= artifact.space_required

        return f"{collector_name} purchased {artifact_name} for a price of {artifact.price:.2f}."

    def remove_artifact(self, artifact_name: str):
        artifact = [a for a in self.artifacts if a.name == artifact_name]
        if not artifact:
            return "No such artifact."
        artifact = artifact[0]
        self.artifacts.remove(artifact)

        return "Removed " + artifact.artifact_information()

    def fundraising_campaigns(self, max_money: float):
        viable_for_fundraising = [c for c in self.collectors if c.available_money <= max_money]
        for collector in viable_for_fundraising:
            collector.increase_money()
        return f"{len(viable_for_fundraising)} collector/s increased their available money."

    def get_auction_report(self):
        total_sold = 0
        result = ["**Auction statistics**"]
        collectors_info = []
        sorted_collectors = sorted(self.collectors, key=lambda c: (-len(c.purchased_artifacts), c.name))
        for collector in sorted_collectors:
            total_sold += len(collector.purchased_artifacts)
            collectors_info.append(collector.__str__())
        result.append(f"Total number of sold artifacts: {total_sold}")
        result.append(f"Available artifacts for sale: {len(self.artifacts)}")
        result.append('***')
        result.extend(collectors_info)

        return '\n'.join(result)

