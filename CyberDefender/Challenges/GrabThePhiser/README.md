# GrabThePhisher
`kit` `phishing` `OSINT` `Threat Intel`
<br>
<br>

GrabThePhisher's scenario is set to be similar to a real-world case involving the PancakeSwap website, the only different is the phishing method. In this challenge the phisher create a similar-looking website aas the real PancakeSwap and make the user import their metamask wallet by pretend to 'log-in' to their metamask account. The Evidence tree are as below:

<p align=center>
    <img src=./img/q1.png width=30%>
</p>

#### Q1. Which Wallet is used for asking the seed phrase?  
> Metamask  

We can see by the website they build and the phishing method they choose, the wallet used for asking the seed phrase is metamask.
<br>

#### Q2. What is the file name that has the code for the phising kit?  
> metamask.php

Inside the `metamask`folder, we can find a php with the name `metamask.php`. That's the file that the phisher used to collect the victims information.
<br>

#### Q3.In which language was the kit written?
> php

By 'the kit' it refers to the `metamask.php`, the code that handle the input and then send it to the phisher.
<br>

#### Q4. What service does the kit use to retrieve the victim's machine information? 
> sypex geo
<P>
    <img src=./img/q4.png>
</p>

We can see in the first few lines in the `metamask.php`, it use an api from a service called `sypex geo`. Upon further research, [sypex geo](https://github.com/hostbrook/sypex-geo) is a database of IP-location that can be integrated using php. 
<br>

#### Q5. How many seed phrases were already collected?
> 3
<p>
    <img src=./img/q5.png>
</p>

In the `log` folder, exist a file called `log.txt` that log seed phrase from a successfull phishing attempt it made, in total they already got 3 seed phrases.
<br>

#### Q6. Write down the seed phrase of the most recent phising incident?
> father also recycle embody balance concert mechanic believe owner pair muffin hockey

Because the php store a new ticker and using APPEND method, the newest data they get will be written below the previous one, which mean the most recent data they got is at line 3.
<br>

#### Q7. Which medium had been used for credential dumping?
> telegram
<p>
    <img src=./img/q7.png>
</p>

We can see the function `sendTel` there is using `Telegram Bot API`, with this information we can now know the data that they've successfully gathered will be send and dump to a Telegram chat using Telegram Bot API.
<br>

#### Q8. What is the token for the channel?
> 5457463144:AAG8t4k7e2ew3tTi0IBShcWbSia0Irvxm10

The image on **Q7** shows the `token` value it use to send the message to the Actor.
<br>

#### Q9. What is the chad ID of the phisher's channel?
> 5442785564

The image on **Q7** shows the `id` value it use to send the message to the Actor.
<br>

#### Q10. What are the allies of the phish kit developer?
> j1j1b1s@m3r0
<p>
    <img src=./img/q10.png>
</p>

There is a commented section in the code saying a few word to the Actor from the kit creator, we can see the developer there.
<br>

#### Q11. What is the full name of the Phish Actor?
> Marcus Aurelius

I was kinda confuse on how to find them, I tried to looking for clue from other folders and files, and eventually come back to `metamask.php`. I noticed they use Telegram BOT API and decided to search about the endpoint API available with the required param chat_id. This is because if the `sendMessage` need a chat_id to specify the receiver, then if I want to know the receiver or owner of that id, the Endpoint must have also required `chat_id`. I searched here for some time https://core.telegram.org/bots/api 

I found an Endpoint API taht required chat_id called `getChat`, following the method to the message, I modify the URL a little bit until it looks like this.

```bash
curl https://api.telegram.org/bot5457463144:AAG8t4k7e2ew3tTi0IBShcWbSia0Irvxm10/getChat?chat_id=5442785564
```
<p>
    <img src=./img/q11.png>
</p>

in the JSON Returned there, we can see the answer for **Q11** and **Q12**.
<br>

#### Q12. What is the username of the Phish Actor?
> pumpkinboii

The answer can also be found in previous question curl result.

### Conclusion

This challenge gives me a new insight on how to do Objective research and forces me (a little bit) to undestand the PHP code, since I'm not too familiar with it. I learned a lot about API and PHP in this challenge! :smirk: