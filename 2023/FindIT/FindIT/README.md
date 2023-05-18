# Fint IT
`Inspect Element`, `Hidden Directory`
<br>
<br>

This challenge is quite simple, might be a little confusing for the last part, we're given a website that show nothing, of course at first when can see its source by using `CTRL + U`, just like that we got our first part of the flag

```html
<!-- 1: FindITCTF{F1nd_tH3_ -->
```

Next, I inspect the `style.css` and get the 2nd flag,

```css
/*2: c0mM0n_ */
```

I then go to the next src available which is `script.js` and find the 3rd part of the flag

```javascript
function randomFlag(){
    return "3: un53cure3_";
}
```

Given no information upon finding the first 3 part of the flag, I checked the cookie section of the website and found the 4th flag in the cookie with the value of `Pl4c35_t0_h1d3_`, but it's not the last part. After reading the description carefully, it said there was a robot `here`, I finally get it that the `robots.txt` is not located in the IP Website, rather it located in the ctf website with the value of `5tuFf_r16ght}`

With that the flag is as below:
```
FindITCTF{F1nd_tH3_c0mM0n_un53cure3_Pl4c35_t0_h1d3_5tuFf_r16ght}
```