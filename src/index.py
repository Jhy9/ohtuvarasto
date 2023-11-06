from varasto import Varasto


def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)
    print("Luonnin jälkeen:"
    f"\nMehuvarasto: {mehua}"
    f"\nOlutvarasto: {olutta}"
    "\nOlut getterit:"
    f"\nsaldo = {olutta.saldo}"
    f"\ntilavuus = {olutta.tilavuus}"
    f"\npaljonko_mahtuu = {olutta.paljonko_mahtuu()}"
    "\nMehu setterit:"
    "\nLisätään 50.7")
    mehua.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {mehua}"
    "\nOtetaan 3.14")
    mehua.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehua}"
    "\nVirhetilanteita:"
    "\nVarasto(-100.0);")
    print_huono(olutta, mehua)

def print_huono(olutta,mehua):
    huono = Varasto(-100.0)
    print(str(huono) + "\nVarasto(100.0, -50.7)")
    huono = Varasto(100.0, -50.7)
    print(str(huono) + f"\nOlutvarasto: {olutta}"
    "\nolutta.lisaa_varastoon(1000.0)")
    olutta.lisaa_varastoon(1000.0)
    print(f"Olutvarasto: {olutta}"
    f"\nMehuvarasto: {mehua}"
    "\nmehua.lisaa_varastoon(-666.0)")
    mehua.lisaa_varastoon(-666.0)
    print(f"Mehuvarasto: {mehua}"
    f"\nOlutvarasto: {olutta}"
    "\nolutta.ota_varastosta(1000.0)")
    saatiin = olutta.ota_varastosta(1000.0)
    print(f"saatiin {saatiin}"
    f"\nOlutvarasto: {olutta}"
    f"\nMehuvarasto: {mehua}"
    "\nmehua.otaVarastosta(-32.9)")
    saatiin = mehua.ota_varastosta(-32.9)
    print(f"saatiin {saatiin}"
    f"\nMehuvarasto: {mehua}")
if __name__ == "__main__":
    main()
