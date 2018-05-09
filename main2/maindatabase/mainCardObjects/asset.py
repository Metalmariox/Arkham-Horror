from main2.maindatabase.pCard import PlayerCard


class Asset(PlayerCard):
    def __init__(self, c_name, c_class, c_level, c_type, c_slot, c_traits, c_cost, c_pips, c_text, c_flavor, c_ref):
        super().__init__(c_name, c_class, c_level, c_type, c_slot, c_traits, c_cost, c_pips, c_text, c_flavor, c_ref)
