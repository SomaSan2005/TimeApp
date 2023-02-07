# TimeApp

This program uses Python's Tkinter GUI library to create a window with a black background that displays the current time in real time in the center of the window. The window has a width of 500 pixels and a height of 500 pixels.

The program includes a show_time function which is called every second using `label.after(1000, show_time)` to get the current time in the format `HH:MM:SS` using the `time.strftime()` function. The time is displayed on a label in a window with a black background.

To place the clock exactly in the center of the window, regardless of its size, we use Tkinter's `place` method to place the label relative to the center point of the `window (relx=0.5, rely=0.5)` and anchor it in the center `(anchor=" center")`.

The program uses an infinite `root.mainloop()` to keep the window open until the user closes it.
