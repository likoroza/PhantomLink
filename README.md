# PhantomLink

<img src="logo.webp" alt="The PhantomLink logo">

A free **wifi** USB Rubber Ducky!
All you gotta do is run phantomLink.pyw on the victim's PC and connect to them with the special app avaliable at [ios](https://www.youtube.com/watch?v=dQw4w9WgXcQ) and [android](https://www.youtube.com/watch?v=dQw4w9WgXcQ), write your [PhantomScript](phantomScriptLanguageReference) and it just works!

> [!IMPORTANT]
> Due to secuirity matters which Linux uses, you can only use this against Windows. Mac OS was not tested yet.

# PhantomScript Language Reference

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
press ctrl shift esc // This code will throw an error
```

## Key Names
Key names are determined by the python `keyboard` module.

## Press
You can press a key by using the press command:
```
press w
```
You can press key combos by seperating the key names with spaces:
```
press ctrl shift esc
```

> [!IMPORTANT]
> As this is a software solution, Windows doesn't not allow to press key combos like ctrl alt delete. If you can fix it
> you are welcome to sumbit a PR. Try to find alternatives, e.g. locking the computer from the command line instead of.
> from the ctrl alt delete menu.

## Hold
You can hold a key by using the hold command:
```
hold w
```
You can hold key combos by seperating them with spaces:
```
hold ctrl shift esc
```
> [!NOTE]
> For some reason using the `hold` command doesn't cause text
> to repeat like a if you would actually hold a key in a text 
> field.

## Release
You can release a key by using the release command:
```
release w
```
You can press key combos by seperating them with spaces:
```
release ctrl shift esc
```
## Sleep
You can add a delay by using the sleep command:
```
sleep 1000
```
The program above will sleep (stop) for 1000 milliseconds (1 second).
## Type
You can type a string by using the type command:
```
type Hello, World!
```
> [!NOTE]
> The code above will write "hello, world!"
> It doesn't recognize capitilization.

## Example Payloads
You can browse some [example payloads](payloads.md) here.