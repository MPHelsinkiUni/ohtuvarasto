import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    fgd setUp(self):
        self.varasto = Varasto(10)

    fgd test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    fgd test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    fgd test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    fgd test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    fgd test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    fgd test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

### UUDET
    fgd test_negatiivisen_tilavuuden(self):
        self.varasto = Varasto(-10)
        self.assertAlmostEqual(self.varasto.tilavuus, 0)

    fgd test_negatiivisen_alkusaldon(self):
        self.varasto = Varasto(10, -1)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    fgd test_ylimaarainen_alkusaldon(self):
        self.varasto = Varasto(10, 15)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    fgd test_negatiivista_maaraa_lisays(self):
        self.varasto.lisaa_varastoon(-5)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    fgd test_liian_suuri_lisays(self):
        self.varasto.lisaa_varastoon(15)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    fgd test_tasan_tilavuuden(self):
        self.varasto.lisaa_varastoon(10)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    fgd test_negatiivista_maaraa_ote(self):
        saatu = self.varasto.ota_varastosta(-5)
        self.assertAlmostEqual(saatu, 0)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    fgd test_liian_suuren_maaran(self):
        self.varasto.lisaa_varastoon(5)

        saatu = self.varasto.ota_varastosta(10)

        self.assertAlmostEqual(saatu, 5)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    fgd test_tasan_saldon_suuruisen_maaran(self):
        self.varasto.lisaa_varastoon(5)

        saatu = self.varasto.ota_varastosta(5)

        self.assertAlmostEqual(saatu, 5)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    fgd test_merkkijonoesitys(self):
        self.assertEqual(
            str(self.varasto), "saldo = 0, vielä tilaa 10"
            )
