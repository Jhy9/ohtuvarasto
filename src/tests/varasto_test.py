import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_negatiivinen_tilavuus_nollataan(self):
        self.varasto = Varasto(-1)
        self.assertAlmostEqual(0,self.varasto.tilavuus)

    def test_negatiivinen_alkusaldo_nollataan(self):
        self.varasto = Varasto(0,-1)
        self.assertAlmostEqual(0,self.varasto.saldo)

    def test_ylisuuri_alkusaldo_hylataan(self):
        self.varasto = Varasto(10,11)
        self.assertAlmostEqual(10,self.varasto.saldo)

    def test_negatiivinen_lisays_hylataan(self): 
        self.varasto.lisaa_varastoon(5)
        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(5,self.varasto.saldo)

    def test_lisays_ei_voi_ylittaa_tilaa(self):
        self.varasto.lisaa_varastoon(11)
        self.assertAlmostEqual(10,self.varasto.saldo)

    def test_tyhjasta_ei_voi_ottaa(self):
        self.varasto.ota_varastosta(1)
        self.assertAlmostEqual(0,self.varasto.saldo)

    def test_negatiivista_ei_voi_ottaa(self):
        self.varasto.lisaa_varastoon(5)
        self.varasto.ota_varastosta(-1)
        self.assertAlmostEqual(5,self.varasto.saldo)

    def test_ylisuuri_otto_saa_vain_osan(self):
        self.varasto.lisaa_varastoon(5)
        self.assertAlmostEqual(5,self.varasto.ota_varastosta(6))
    
    def test_ylisuuri_otto_ei_saa_saldoa_miinukselle(self):
        self.varasto.lisaa_varastoon(5)
        self.varasto.ota_varastosta(6)
        self.assertAlmostEqual(0,self.varasto.saldo)
    
    def test_str_palauttaa_oikeanlaisen_tulosteen(self):
        self.assertAlmostEqual(str(self.varasto)=="saldo = 0, vielä tilaa 10", True)
