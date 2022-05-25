from FloryCanbusMessage import FloryCanbusMessage

# PGN 65266


class FuelEconomyLiquid_65266(FloryCanbusMessage):

    def __init__(self, pgn, data):
        super().__init__(pgn, data)

    def load_dictionary(self, model_id=None):
        self.dictionary["FuelRate"] = int.from_bytes([int(self.data[1], 16), int(self.data[0], 16)], "big") * 0.05
        # self.dictionary["Engine Instantaneous Fuel Economy [km/L]"] = int.from_bytes([int(self.data[3], 16), int(self.data[2], 16)], "big") * (1.0/512.0)
        # self.dictionary["Engine Average Fuel Economy [km/L]"] = int.from_bytes([int(self.data[5], 16), int(self.data[4], 16)], "big") * (1.0/512.0)
        # self.dictionary["Engine Throttle Valve 1 Position 1 [%]"] = int(self.data[6], 16) * 0.4
        # self.dictionary["Engine Throttle Valve 2 Position 1 [%]"] = int(self.data[7], 16) * 0.4
