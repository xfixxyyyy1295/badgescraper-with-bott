const Discord = require('discord.js');

exports.run = async (client, message, args) => {
  
  message.channel.send('Bu bir Örnektir!')
  
};

exports.conf = {
  enabled: true,
  guildOnly: false,
  aliases: ['ornek'],
  permLevel: 0
};

exports.help = {
  name: 'örnek',
  description: 'örnek',
  usage: 'örnek'
};