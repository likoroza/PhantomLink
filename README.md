# PhantomLink

<img src="logo.webp" alt="The PhantomLink logo">

A free **wifi** USB Rubber Ducky!
All you gotta do is run phantomLink.pyw on the victim's pc and connect to them with the special app avaliable at [ios](https://www.youtube.com/watch?v=dQw4w9WgXcQ) and [android](https://www.youtube.com/watch?v=dQw4w9WgXcQ), write your [PhantomScript](phantomScriptLanguageReference) and it just works!

# PhantomScript Language Refernce

## Info
Originally we wanted to use DuckyScript, but because of copyright issues we
settled on a new language based on it, PhantomScript. Don't worry, moving to it
is intuitive and easy.

## Comments
To make comments you can either use `#` or `//` at the beginning of the line:
```
# This code will not be run
// This is a comment
```
For now you are not allowed to use comments in the middle of a line.
```
TEMP_CODE // This code will throw an error
```

## Key Names
Key names are determined by the python `keyboard` module.

## Press
You can press a button by using the press command:
```
press w
```
You can press key combos by seperating them with spaces:
```
press ctrl shift esc
```

> [!IMPORTANT]
> As this is a software solution, Windows doesn not allow to press key combos like ctrl alt delete. If you can fix it
> you are welcome to sumbit a PR. Try to find alternatives, e.g. locking the computer from the command line instead of.
> from the ctrl alt delete menu.