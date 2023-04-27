# Celeste Speedrunning Association
`EPOCH` 
<br>
<br>

This challenge website told us to beat the record holder, now we just play by going to the `/play` directory. There is a button there, but I want to see the source code first.

```html
<form action="/submit" method="POST">
  <input type="text" style="display: none;" value="1682610044.152733" name="start" />
  <input type="submit" value="Press when done!" />
</form>
```

You can see that there is a `"start"` with the value of epoch time there, I assume when we press the button it'll count as the `finished time`, we can't edit the finish time can we? but we can edit the start value yes :smile:

we can use this epoch to make our `start time` in the future, thus make the speedrun in negative times.

```
Epoch timestamp: 1682697028
Timestamp in milliseconds: 1682697028000
Date and time (GMT): Friday, April 28, 2023 3:50:28 PM
Date and time (your time zone): Friday, April 28, 2023 10:50:28 PM GMT+07:00
```

In firefox you, when you go to network tab, you can do `edit and resend` a request, we are going to do that, with the value of the start `1682697028`, and yes, we got the flag.

```
actf{wait_until_farewell_speedrun}
```