from abc import ABC, abstractmethod

class BaseScraper(ABC):
    def run(self):
        raw = self.fetch()
        self.save(raw)

    @abstractmethod
    def fetch(self):
        pass

    @abstractmethod
    def parse(self, raw):
        pass

    def Initial_Clean(self, parsed):
        return parsed

    def save(self, df):
        df.to_csv("output.csv")