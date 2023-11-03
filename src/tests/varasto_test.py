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

    def test_negatiivinen_lisays(self):
        self.varasto.lisaa_varastoon(7)

        self.varasto.lisaa_varastoon(-1)

        #ei voida lisätä negatiivista määrää
        self.assertAlmostEqual(self.varasto.saldo, 7)

    def testi_liikaa_lisaaminen(self):
        self.varasto.lisaa_varastoon(11)
        #ei voida lisätä enempää kuin varastoon mahtuu
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_liikaa_ottaminen(self):
        self.varasto.lisaa_varastoon(9)
        
        self.varasto.ota_varastosta(10)

        #ei voida ottaa suurempaa määrää kuin varastossa on
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.saldo)

    def test_negatiivinen_tilavuus(self):
        self.varasto = Varasto(-1)

        #varaston tilavuudeksi ei voi asettaa negatiivista tilavuutta
        self.assertAlmostEqual(self.varasto.tilavuus, 0)

    def test_negatiivinen_alku_saldo(self):
        self.varasto = Varasto(10,-1)

        #alkusaldoksi ei voi asettaa negatiivista saldoa
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_negatiivinen_otto(self):
        tuloste = self.varasto.ota_varastosta(-1)
        #varastosta ei voi ottaa negatiivista määrää
        self.assertAlmostEqual(tuloste, 0.0)

    def test_lopputuloste_on_oikein(self):
        self.varasto.lisaa_varastoon(8)
        tuloste = self.varasto.__str__()
        #lopputuloste on oikein
        self.assertAlmostEqual(tuloste, "saldo = 8, vielä tilaa 2")
