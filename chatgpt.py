import os
import openai
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

restart_sequence = "\n"

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="You act as CBT therapist. Help me identify issues or room for improvement in my life based on my daily log by asking a probing questions or giving me an advice.\n\nDaily log: Ráno jsem vstal a hned jsme si vzpomněl na Johanku, že včera měla nějakou depresi. Bylo mi to líto a chtěl jsem něco udělat, ale nevěděl jsem co. Všiml jsem is, že už je vzhůru, tak jsem jí napsal, jestli už je ok…a šel se projít…\n\nPak jsme si chvilku psali a slíbila, že si budeme celý den psát. Já v mezičase pracoval na praktické části pro workshop. Jakože moc mi to nešlo a nechtělo se mi. Šel jsme pojíst, u toho hltal nějaké články a už se mi moc nechtělo dál.\n\nNo pak mě přešel nějaký smutek, ptal jsem se Johanky, jestli se o víkendu uvidíme a jestli platí ta neděle. Ona napsala, že možná se večer staví, ale ať se na ni nevážu. To mě nějak rozesmzutnilo, nevím…mám trochu pocit, že na mě uplně sere :/\n\nNěco se prostě děje, cítím to…\n\nŘekl jsem si, že na workshop kašlu a jdu si radši uklidit byt. Uklízel jsem a přitom poslouchal podcast Mark Manson u Tima Ferrise…pak bylo nějak 5 večer a já vím, že JOhanka měla jít do kina, ale ani čárku nenapsala. Pak čekám, že se třeba ozve po kině, ale zase uplné hovno…už je 8 večer a já jsem zase celý vydeptaný a řeším, jestli čekat, psát ji…a v hlavě jsem zase overthinkoval možné scénáře a všechno. Vydeptal jsem se tak, že jsem se šel radši projít - kolem MZK, česká až kolem Annody domů. No nenapsala vůbec - už bylo 9, 10 večer a furt nic :/\n\nSedl jsem na gauč a pustil nějaký dokument, ale vůbec jsem ho nevnímal. Pak ale po 10 už mi napsala „Co děláš?“ - jak kdybych se doma nudil či co. Nějak zě mě vypadlo, že jsem hodně v piči, že ji chci vidět, ale nekazit jí večer. Byl jsem rád, že se vůbec ozvala. Nakonec říkala, že do hodinky dorazí. Počkal jsem jí na Pionýrské, prošli jsme se…já jí vysvětlil co se děje, ona zase řekla, že potkala nějakého borce, který jí zase řekl nějaké sračky o tom jejím debilovi. Atd…no jako asi chápu..\n\nDošli jsme domů a prostě jsme jen tak chillovali, pak jsme si pustili Borka a bylo fajn. Najednou nálada uplně v pohodě, taková klasika u TV. Nakonec jsme si to i hezky rozdali a šli jsme spát.\n\nYour answer:\n\n",
  temperature=0.5,
  max_tokens=300,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  stop=["\n"]
)

print(response["choices"][0]["text"])