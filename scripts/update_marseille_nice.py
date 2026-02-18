#!/usr/bin/env python3
import re

# New URLs for Marseille (Old Port) and Nice (Blue Chairs)
new_urls = {
    'marsilya': 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=800&photo_reference=AZLasHq1tlw-Yii-xWhsrmLNOWe_cikkWSE680N7Xr8CB0c1dcPsfWaCSsOxjkBWBvqU2g5Q5sAAHt55dk37ecdmg3mpYXG5GIjVz9-5rVR_mOA9I2Nb2tt1FTvrNUHCKde4ke3C14HUZU2QhtbdprB5MLG2wL8rd4LOCAlehl-Hgx5BuzUqZIeK6_GU5dBklMHpKZ8lQbgOgbSICtLgPyk4z0prjEx02f7c9JebwfluF5bjfrP8f4zXwDhcoGYYHSgdm33yFMtEO3F-XeeGEzGY7YomDmQq80x_W4AsWWxc1o8Y1E4jv-71-ylLgLFOQQrdXAmnmLUDPvOmGHvmG4ccHmArC5pV1rmuhonMB1P7GWXf4IKLUVGd2dZsmPhIcne_3zniu0I7xnofJM2yEghQkdaLhCin7ZkCjDcPTtlGhmdIWU_s18tMl977-4yA9zBCXqAIBOEOsqO2IJBFDEMg0qNiVlVBRoubi1HI795mw8i15TM-I6bqkmj4nTG5JiZWD87rG8h0jdkiCDvghF9fZvOnTx4SnqPQ7xbo4iEFwZFFNVnZvgr170Hugqnha8xlXenPhyM0-9VhFA&key=AIzaSyBOXbf-5v4aXyEYgciwX4EfPYAGXX6Yy9g',
    'nice': 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=800&photo_reference=AZLasHpdRI5hwfjXIQ1UsB4jrNjpb5E62YbiSvubafP7wNtISYylo0TO3T7yDEzFmGAAsnkzCJbgpmiqGPUWPhCwtpLD_59Qd8WmeG4UpjC53TlsCkQng4kGeGuexsMfOW37VUzZiDV7JcwsVoC9xtMi53dDvLFh5hmTyCrRJcjex9olao7ii7nZWr8a4mId6dqBNlKFD7NwOFvEKJFedrnvCB6A1RQ0LYnixSfrauq3rXAS62WfYt2gI-M1civmVfNA4hKkiFCHSfOxauAZULeyKVaqzqGguVdtIpefv80emm-YAbZ7aNSeMJ8kn0Xs0X1-DFdmcTZ1qFQSPBYQL5vsNKjQySCaurtq5NdQiHbbJtJpQJUQYuBPyHvka6wPzjUQ2HeCmNWyWr0VMGj-iQRO5ZuFhDFwBdODa9iWKzTOO4Chy-UrWfzsDdDKUEPXqpuMef4zQt743EFnrBj6YkGltlZ_LIUfl6PZ1xs3ya9QQb8oxPZDqW2RmK112BqwPMrbpcdrhvFJTbAaoGVDfqzmaW7Xie2IYIJSdZoiFZrsmiHxh-u-wqmX8ZDk5MU7B0hkzaVVhrzanjKglANHQW0xGG40faNgKA&key=AIzaSyBOXbf-5v4aXyEYgciwX4EfPYAGXX6Yy9g',
}

files = ['lib/screens/city_switcher_screen.dart', 'lib/screens/explore_screen.dart']

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for city_id, url in new_urls.items():
        # Pattern for networkImage in city_switcher
        pattern1 = rf'("id":\s*"{city_id}"[^}}]*"networkImage":\s*")[^"]+(")' 
        content = re.sub(pattern1, rf'\g<1>{url}\g<2>', content)
        
        # Pattern for _cityImages in explore_screen
        pattern2 = rf"('{city_id}':\s*')[^']+(')"
        content = re.sub(pattern2, rf"\g<1>{url}\g<2>", content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print('✅ Marsilya ve Nice fotoğrafları güncellendi!')
print('   Marsilya: Old Port (Vieux Port)')
print('   Nice: Mavi Sandalyeler (Chaises Bleues)')
