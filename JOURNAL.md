| Title | Author | Description | Date Started |
| ------------- | ------------- | ------------- | ----------|
| Elemental Designs Keyboard | @samatua1221-2896 | A custom mechanical keyboard | 7/20/25 |

# July 20, 2025 (7 hrs)

So I've actually spent a lot of time wanting to have my own keyboard for a while now (especially when dealing with the thing that Apple calls its keybaord for ipads *cough**cough*ipad folio*cough**cough*) but this is really something I don't have too much experience in but plan on getting it down pretty easily. As of now I've already worked to design a couple of PCBs, one for hackpad and one for my own 3D pen, so seeing that majority of a keyboard is just the PCB I'm looking forward to this.

So far my plan is to have an almost full keboard layout with some adjustments like getting rid of the f keys and adding two rotary encoders. I'll have some of the usual keys transformed maybe into custom shortcut keys for CADding since that's what I'll probably doing most with the keyboard. 

<img width="1920" height="1080" alt="Screenshot 2025-07-03 4 39 58 AM" src="https://github.com/user-attachments/assets/b73e7997-488c-46b8-9a61-788bdbf4c344" />

This is how I think I'll be formatting my keyboard so far so I'll go with this and make a DXF file to align all of my switches on my PCB.

*A couple hours later*

So after doing all of that, I started to work on my schematic for my project itself. I don't really know too much about how to make a schematic for a keyboard so I ended up doing a little but of research which did help me a little bit in understanding what to do. I'll be using a RasPi Pico as my brain and pretty standard cherry mx switches for all of my keys. I still haven't decided whether I should make custom keycaps or just 3D print them in the end. I'll end of figuring all that out later. 

<img width="1920" height="1080" alt="Screenshot 2025-07-03 11 03 11 AM" src="https://github.com/user-attachments/assets/3cdf1953-faa1-4299-9b12-40b9069dfaea" />
<img width="1920" height="1080" alt="Screenshot 2025-07-03 7 23 07 PM" src="https://github.com/user-attachments/assets/d4de5dec-dee7-4d12-9ce5-32b76643585c" />

So this is how I laid out my whole design for my schematic, I checked a couple of sources and ran ERC a couple of times, so far it looks all good so tomorrow I'll move onto working on the rest of the PCB board itself.

# July 21, 2025 (8 hrs)

So I can now see why everyone doesn't like making PCB boards for keyboards like this. I ended up loading up all the footprints into KiCad and oh my god are there a lot of switches I have to place. Using the DXF file I made yesterday I spent all of 2 hours trying to align all of the switches in the correct places when I realized at the end, OH, I accidentaly named my two rotary encoders switches so I'm missing two *face palms* so I decided to do away with two of the shortcut keys just to keep moving forward because of the event time contraints. 

<img width="1920" height="1080" alt="Screenshot 2025-07-04 6 27 06 PM" src="https://github.com/user-attachments/assets/b83326ce-85cf-405a-8b42-867d53f56269" />
<img width="1920" height="1080" alt="Screenshot 2025-07-08 3 19 30 AM" src="https://github.com/user-attachments/assets/86426a00-46e4-4735-b60f-155eb82539f0" />
<img width="1920" height="1080" alt="Screenshot 2025-07-20 1 03 57 PM" src="https://github.com/user-attachments/assets/6fc1c31c-30cf-429e-8593-6a64933d5797" />

So after a long time everything looks pretty good to start wiring except its absolute madness with all of this. At this point, I thought it was pretty standard to deal with this much wiring but I ACTUALLY learned later that it would've been so much easier if I had wired my matrix differently but oh well, it is what it is now. Today I spent a lot of time going through all of the intense stuggle of wiring and still haven't finished so tomorrow will probably be the day I finish it.

# July 23, 2025 (6 hrs)

So today I ended up finishing all of the wiring on the keyboard and after using an unhealthy amount of vias, I finally was able to pass the DRC check. I decided that I had a little extra time on my hands and I do want to try and get that 1 extra point in highway just for the extra design and extra effort put in so I decided to add some silkscreen that I designed myself as well as my own logo to the front of the PCB which was also another first of mines. I spent most of today trying to figure out the dimensions of everything and adding in other things like the stabilizers for my longer keys and other things.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/350ec3c0-5733-4fb9-9f09-72e7343d604d" />

# July 24 (2 hrs)

So I ended up forgetting that I needed to put the stabilizers in which led to a whole lotta rerouting on my part for all the routing that apparently led straight into drill holes (yayy). After that, I pretty much started on making the base for my keyboard, I decided that I would be using dovetail connections since I need to split my keyboard in half when it gets #D printed by printing legion.

<img width="1920" height="1080" alt="Screenshot 2025-07-24 11 36 29 PM" src="https://github.com/user-attachments/assets/167473a6-32a9-4e79-a1d9-3d2eb431892b" />

# July 25, (7 hrs)

So today I spent majority of my time getting everything working in CAD. Unfortunately, I realized too late that I could just add all of my switches into KiCAD to spare me much headache later in the process, but it all worked out eventually. Most of my time was spent getting the models from GrabCAD to place in Onshape since thats the software I usually use and making sure that the PCB was all good for me to place all of my THT components into. After that, I then made the decision that I wanted custom keycaps for all of my switches. Right now, buying my own keycaps would be pretty expensive for shipping and just getting them from printing legion seemed like the right thing to do, plus it would let me add my own touch of design into the process. I decided to make caps that were rounded at the top just for a more aesthetic feel, I also decided at this point that I might want a more open layout of my case because I want to show off the PCB itself and the silkscreen on it. 

<img width="1920" height="1080" alt="Screenshot 2025-07-25 9 09 05 PM" src="https://github.com/user-attachments/assets/1c25b54e-afbf-4ed9-b9e3-fd09af7560f0" />

After that, I started to work on the case itself. I did notice that it would be harder for me to create a top for the case due to the whole keyboard, so I would go for an open layout. Due to this, I decided that it would be better for me to add some custom art straight into the case fitting with the whole elemental thing as well. I spent a couple hours looking into it, but I was able to draw up a sun and moon on my ipad in Adobe Fresco and convert it from a png to a dxf on an online converter. After that, it took a little while to play around with it but I was able to make my custom art lifted a little bit from the floor of the bottom of the case, also providing a little more thickness between the ground and the PCB. Even though it'll be covered up, it's a nice thing to have in the case that I ever switch out the PCB if I were to make another keyboard or using it as a case for another type of electronic.

<img width="288" height="1379" alt="Sun Moon" src="https://github.com/user-attachments/assets/c0fdaa21-cb21-4b77-b6e3-a7a34b29b2e3" />
<img width="1920" height="1080" alt="Screenshot 2025-07-26 12 37 23 AM" src="https://github.com/user-attachments/assets/d1ddc809-3070-4cd2-9b1e-a7a250d7b1df" />
<img width="1920" height="1080" alt="Screenshot 2025-07-26 12 37 21 AM" src="https://github.com/user-attachments/assets/85b0c6f4-6c5f-4511-bd70-2ab80c3ff1ce" />

After that, I spent a little but more time smoothing out the edges and making sure the case looks pretty good. The hardest part was splitting the case after the design was on their to make sure the design lines up on both pieces since they're being printed separetely.

I ended up being able to but the PCB into the keyboard case just to check if it fits and yayy it works, tmr I'll spend more time finshing up the whole keyboard layout and all the custom keycaps, maybe starting on my BOM so I can get my submission in.

<img width="1920" height="1080" alt="Screenshot 2025-07-26 12 36 59 AM" src="https://github.com/user-attachments/assets/cbefb673-2c06-4781-baa8-3ef2e4e1a2fb" />

# July 26, 2025 (4 hrs)

Spent most of today finishing up the touches and adding the final keys and keycaps, all of them will be custom with three different sizes, also added a slot for the cable to be attached to the RasPi since I forgot that earlier too, looks pretty good, going to start sourcing parts now and making the final submission.

<img width="1920" height="1080" alt="Screenshot 2025-07-26 4 57 49 PM" src="https://github.com/user-attachments/assets/8c6d8fc0-b0cb-4eb4-b39a-873901718dbd" />

