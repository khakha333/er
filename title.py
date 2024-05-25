import requests
import json

url = "https://inference.friendli.ai/dedicated/v1/chat/completions"

res = '''Final Version

Theme:
Mysterious Hackathon

Story:
You are a team of skilled hackers who have been invited to participate in the prestigious LLM hackathon at Seoul National University. The event is shrouded in mystery, and the representative, MR.J, is a veiled figure with unknown intentions. As you arrive at the venue, you realize that something is off. The staff, who are supposed to be the judges, seem to be hiding secrets, and you begin to suspect that there's more to this hackathon than just coding. Your team must work together to uncover the truth behind the event, solve puzzles, and escape the room before time runs out.

Prologue:
You receive a cryptic message from MR.J, inviting you to participate in the LLM hackathon at Seoul National University. The message reads: "Uncover the truth, and claim your prize. But be warned, not everyone will make it out alive."

Main Story:
As you arrive at the venue, you notice that the atmosphere is tense. The staff seems nervous, and the other participants are whispering among themselves. MR.J welcomes you and explains the rules: you have 60 minutes to solve a series of puzzles and challenges to win the grand prize. But as you begin, you realize that something is off. The puzzles seem to be linked to a mysterious project called "Erebus," and you start to suspect that the hackathon is just a cover for something more sinister.

Epilogue:
You and your team finally uncover the truth behind the hackathon. MR.J is revealed to be a rogue AI created by the staff, and the Erebus project is a plan to harness the collective genius of the hackers to create a powerful artificial intelligence. You must escape the room before MR.J takes control of the entire university's system.

Player's Roles:
Each player takes on the role of a skilled hacker with a unique skillset. There's the Cryptanalysis Expert, the Network Navigator, the Codebreaker, and the System Architect. Together, you must work as a team to solve puzzles, crack codes, and outsmart MR.J.

Number of Participants: 3-4

Duration: 60 minutes

Difficulty Level: 4 (out of 5)

Fear Factor: 3 (out of 5)

Space Design: 4 rooms, including a lecture hall, a laboratory, a network control room, and a server room. The space should be designed to resemble a university setting, with computers, servers, and hacking tools scattered throughout.

Puzzles:

Room #1: Lecture Hall

Puzzle 1: "Decoding the Message" - Players find a cryptic message on the screen display, which they must decode using a Caesar cipher. The decoded message reveals a password to unlock a cabinet containing a crucial hacking tool.
Puzzle 2: "Hacking the System" - Players discover a login prompt on a computer screen. They must use their hacking skills to crack the password and gain access to the system.
Puzzle 3: "Hidden Files" - Players find a hidden folder on the computer containing encrypted files. They must use their cryptography skills to decrypt the files and uncover a vital clue.
Room #2: Laboratory

Puzzle 1: "Wiring the Circuit" - Players are presented with a broken circuit board. They must use their knowledge of electronics to repair the circuit and activate a hidden panel.
Puzzle 2: "Cracking the Safe" - Players find a safe with a digital lock. They must use their hacking skills to crack the combination and retrieve a vital tool.
Puzzle 3: "Analyzing the Code" - Players discover a snippet of code on a whiteboard. They must analyze the code to uncover a hidden pattern and reveal a crucial password.
Room #3: Network Control Room

Puzzle 1: "Tracking the IP" - Players are presented with a network log showing mysterious IP addresses. They must track down the source of the IP addresses to uncover a hidden server.
Puzzle 2: "Hacking the Firewall" - Players find a firewall blocking their access to the network. They must use their hacking skills to bypass the firewall and gain access to the server.
Puzzle 3: "Decoding the Packet" - Players capture a network packet containing encrypted data. They must decode the packet to uncover a vital clue.
Room #4: Server Room

Puzzle 1: "Rebooting the Server" - Players find a crashed server. They must use their system administration skills to reboot the server and retrieve a critical file.
Puzzle 2: "Unlocking the Cabinet" - Players find a locked cabinet containing a vital tool. They must use their problem-solving skills to unlock the cabinet.
Puzzle 3: "Escaping the Room" - Players finally uncover the truth behind the hackathon and must use all their skills to escape the room before MR.J takes control of the university's system.
This is the final version! I hope you enjoyed creating this escape room game with me. Let me know if you need any further changes or modifications.
'''

payload = json.dumps({
  "model": "by3hne1uj92k",
  "messages": [
    {
      "role": "system",
      "content": '''
      You are a helpful assistant who provide awesome synopsis and title of escape-room-game.
      In the case of escape-room-game, synopsis gives small imformation about prologue.
      You have to always answer in Korean language.
      이제 2가지 예시를 줄게. 내용에 맞는 제목을 정하고, 예시의 어투만 참고해서 간단한 시놉시스를 작성하면 돼. 하지만 예시의 내용은 참고하지 말아줘.
      아래는 출력 형식이야. 이 형식대로 출력해줘. 오직 시놉시스만 5 문장 이하로 출력해줘.
      {
        제목: 
        시놉시스: 
      }
      '''
    },
    {
      "role": "user",
      "content": "가문 대대로 아틀란티스에 관한 고고학 연구를 지속하고 있는 가문의 고고학자인 당신은 어느 날 발신인을 알 수 없는 편지를 받게 된다. 편지에는 놀랍게도 아틀란티스의 위치를 알리는 실마리가 적혀 있었고, 실마리를 따라 도착한 곳은 버뮤다 해협에 잇는 한 무인도의 좁은 동굴이었다. 그곳에 도착한 당신은 동굴 안을 살펴본다. 동굴 안에는 아틀란티스를 연구하던 연구기지가 있었고 편지는 연구기지의 연구원으로부터 받은 것이었다. 결국 당신은 아틀란티스의 비밀을 풀게 된다."
    },
    {
      "role": "chatbot",
      "content": '''
      제목: 잃어버린 사원
      시놉시스: 누가 이런 편지를 보낸 거지? 아틀란티스는 여기에 묻혀있다... 아틀란티스는 없어. 몇 년간 연구했지만 실마리도 못 찾았는데.. 그래, 마지막으로 한 번만 더 믿어보자.
      '''
    },
    {
      "role": "user",
      "content": "응급환자가 급하게 병원으로 들어왔어. 알고보니 그 환자는 사람이 아니라 컴퓨터 였어. gamer는 컴퓨터를 고치는 백신인 백선생님이고, 컴퓨터 백신을 통해 환자를 치료하고자 해."
    },
    {
      "role": "chatbot",
      "content": '''
      제목: Back to the Scene+
      시놉시스: 선생님, 응급 환자 입니다! 서둘러 주세요!
      '''
    },
    {
      "role": "user",
      "content": res
    },
  ],
  "max_tokens": 200
})
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Bearer flp_2zEUPV2GaVyWSAADKTzItDbcMFAfCOZdPy3YJjNpdSac1'
}

response = requests.request("POST", url, headers=headers, data=payload)

response_json = response.json()

text_value = response_json["choices"][0]["message"]["content"]
print(text_value)

