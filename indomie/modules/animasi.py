from time import sleep
from indomie import CMD_HELP
from indomie import CMD_HANDLER as cmd
from indomie.utils import indomie_cmd


@indomie_cmd(pattern='sadboy(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`Pertama-tama kamu cantik`")
    sleep(2)
    await typew.edit("`Kedua kamu manis`")
    sleep(1)
    await typew.edit("`Dan yang terakhir adalah kamu bukan jodohku`")

# Create by https://github.com/IndomieGorengSatu


@indomie_cmd(pattern='hujan(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`H`")
    await typew.edit("`Hm`")
    await typew.edit("`Hmm`")
    await typew.edit("`Hmmm`")
    await typew.edit("`Hmmmm`")
    await typew.edit("`Hmmmmm`")
    sleep(2)
    await typew.edit("`Hujan Hujan Gini Ange😔`")
    sleep(2)
    await typew.edit("`Enaknya Coli🤤`")
    sleep(1)
    await typew.edit("`8✊===D`")
    await typew.edit("`8=✊==D`")
    await typew.edit("`8==✊=D`")
    await typew.edit("`8===✊D`")
    await typew.edit("`8==✊=D`")
    await typew.edit("`8=✊==D`")
    await typew.edit("`8✊===D`")
    await typew.edit("`8=✊==D`")
    await typew.edit("`8==✊=D`")
    await typew.edit("`8===✊D`")
    await typew.edit("`8==✊=D`")
    await typew.edit("`8=✊==D`")
    await typew.edit("`8✊===D`")
    sleep(2)
    await typew.edit("`Ahhh🤤`")
    sleep(1)
    await typew.edit("`8✊===D`")
    await typew.edit("`8=✊==D`")
    await typew.edit("`8==✊=D`")
    await typew.edit("`8===✊D`")
    await typew.edit("`8==✊=D`")
    await typew.edit("`8=✊==D`")
    await typew.edit("`8✊===D`")
    await typew.edit("`8=✊==D`")
    await typew.edit("`8==✊=D`")
    await typew.edit("`8===✊D`")
    await typew.edit("`8==✊=D`")
    await typew.edit("`8=✊==D`")
    await typew.edit("`8✊===D`")
    await typew.edit("`crotss💦`")
    await typew.edit("`crotss💦💦`")
    await typew.edit("`crotss💦💦💦🤤`")
    sleep(2)
    await typew.edit("`H`")
    await typew.edit("`Hm`")
    await typew.edit("`Hmm`")
    await typew.edit("`Hmmm😔`")
    sleep(2)
    await typew.edit("`Ini Untuk Yang Terkahir`")
    sleep(2)
    await typew.edit("`Kenapa Ya Gw Coli Tadi😔`")
    sleep(2)
    await typew.edit("`Dah la besok besok ga mau lagi`")

# Create by https://github.com/IndomieGorengSatu


@indomie_cmd(pattern='engas(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("Udah nggak kuat nahan")
    sleep(1)
    await typew.edit("Pengen gitu-gituan")
    sleep(1)
    await typew.edit("Ayo cepat masukkan")
    sleep(1)
    await typew.edit("Jangan lama - lama")
    sleep(1)
    await typew.edit("Pliss cobain")
    sleep(1)
    await typew.edit("Jangan di nanti - nanti")
    sleep(1)
    await typew.edit("Ayo kita happy")
    sleep(1)
    await typew.edit("Tapi pake pengaman")


# Create by https://github.com/IndomieGorengSatu


@indomie_cmd(pattern='ehm(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("Eh..")
    sleep(2)
    await typew.edit("Suara kamu ga jelas")
    sleep(2)
    await typew.edit("Kayanya kalau call pribadi lebih jelas")
    sleep(2)
    await typew.edit("Gamau nyoba?")


@indomie_cmd(pattern='vc(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("Kaa 🥺")
    sleep(2)
    await typew.edit("Temenin vc col*🥺 ")
    sleep(2)
    await typew.edit("Yuu kak temenin :( ")
    sleep(2)
    await typew.edit("Lagi tegang nihh")
    sleep(2)
    await typew.edit("Bentar doang ko 🥺")
    sleep(2)
    await typew.edit("Nanti aku tf deh janjii")

CMD_HELP.update({
    "animasi":
    f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}sadboy`\
    \n↳ : Biasalah sadboy hikss\
    \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}hujan`\
    \n↳ : Coba aja hehehe.\
    \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}engas`\
    \n↳ : sange brutal.\
    \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}ehm`\
    \n↳ : cobain sendiri.\
    \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}vc`\
    \n↳: sagapung."
})
