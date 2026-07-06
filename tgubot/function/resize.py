import asyncio
import os

from PIL import Image
from telethon.tl import types
from moviepy import VideoFileClip
from tgubot.handler.spy import SPY
from traceback import format_exc


@SPY(outgoing=True, pattern=r"^!!rzimg (\d+) (\d+) ?(r)?")
async def imageresizer(E):
    resized_image_path = ".cache/image_resized.png"
    match = E.pattern_match
    width = int(match.group(1))
    height = int(match.group(2))
    reply_flag = match.group(3)
    reply_msg = await E.get_reply_message()
    await E.edit(f"Image Resizer\nWidth: {width}\nHeight: {height}\n(Downloading...)")

    if E.is_reply:
        if reply_msg.media:
            image_path = await E.client.download_media(
                reply_msg.media,
                ".cache/temp_image",
            )

            # Load your image and convert to PNG if necessary
            await E.edit(
                f"Image Resizer\nWidth: {width}\nHeight: {height}\n(Converting...)"
            )
            with Image.open(image_path) as img:
                if img.format in ["JPEG", "JPG", "WEBP"]:
                    img = img.convert(
                        "RGB" if img.format in ["JPEG", "JPG"] else "RGBA"
                    )
                    image_path = ".cache/temp_image.png"
                    img.save(image_path)
                    img = Image.open(image_path)

                    # Resize the image
                    await E.edit(
                        f"Image Resizer\nWidth: {width}\nHeight: {height}\n(Resizing...)"
                    )
                    img = img.resize((width, height))

                    # Save the resized image in PNG format
                    img.save(resized_image_path)
            await E.edit(
                f"Image Resizer\nWidth: {width}\nHeight: {height}\n(Sending...)"
            )
            # Upload the resized video
            if reply_flag == "r":
                await E.client.send_file(
                    E.chat_id, resized_image_path, reply_to=reply_msg.id
                )
            elif not reply_flag:
                await E.client.send_file(E.chat_id, resized_image_path, reply_to=E.id)
            await E.edit("Image resized and uploaded successfully!")
            # await asyncio.sleep(1)
            # await E.delete()
            # Clean up the temporary files
            os.remove(image_path)
            os.remove(resized_image_path)
            if os.path.exists(".cache/temp_image.png"):
                os.remove(".cache/temp_image.png")
            if os.path.exists(".cache/temp_image.webp"):
                os.remove(".cache/temp_image.webp")
            if os.path.exists(".cache/temp_image.jpg"):
                os.remove(".cache/temp_image.jpg")
            # directory = os.path.expanduser('.cache/')
            # delete_all_files_in_directory(directory)
            await asyncio.sleep(1)
    await E.delete()


@SPY(outgoing=True, pattern=r"^!!rzvid (\d+) (\d+) ?(r)?")
async def videoresizer(E):

    match = E.pattern_match
    width = int(match.group(1))
    height = int(match.group(2))
    reply_flag = match.group(3)
    reply_msg = await E.get_reply_message()
    await E.edit(f"Video Resizer\nWidth: {width}\nHeight: {height}\n(Downloading...)")

    if E.is_reply:
        if reply_msg.media:
            try:
                await E.client.download_media(
                    reply_msg.media,
                    ".cache/temp_video.mp4",
                )
                await E.edit(
                    f"Video Resizer\nWidth: {width}\nHeight: {height}\n(Resizing...)"
                )

                # Load your video
                clip = VideoFileClip(".cache/temp_video.mp4")

                # Resize the video
                clip = clip.resized((width, height))

                # Save the resized video
                clip.write_videofile(
                    ".cache/video_resized.mp4",
                    codec="libx264",
                    audio_codec="aac",
                )
                await E.edit(
                    f"Video Resizer\nWidth: {width}\nHeight: {height}\n(Sending...)"
                )
                # Upload the resized video
                if reply_flag == "r":
                    await E.client.send_file(
                        E.chat_id,
                        ".cache/video_resized.mp4",
                        reply_to=reply_msg.id,
                        attributes=[
                            types.DocumentAttributeVideo(
                                duration=int(clip.duration),
                                w=clip.w,
                                h=clip.h,
                                round_message=False,
                                supports_streaming=True,
                            )
                        ],
                    )
                elif not reply_flag:
                    await E.client.send_file(
                        E.chat_id,
                        ".cache/video_resized.mp4",
                        reply_to=E.id,
                        attributes=[
                            types.DocumentAttributeVideo(
                                duration=int(clip.duration),
                                w=width,
                                h=height,
                                round_message=False,
                                supports_streaming=True,
                            )
                        ],
                    )
                await E.edit("Video resized and uploaded successfully!")
            except Exception as e:
                print(format_exc())
                try:
                    await E.edit(e)
                except Exception as e:
                    print(e)

            # Clean up the temporary files
            if os.path.exists(".cache/temp_video.mp4"):
                os.remove(".cache/temp_video.mp4")
            if os.path.exists(".cache/video_resized.mp4"):
                os.remove(".cache/video_resized.mp4")
    await asyncio.sleep(1)
    await E.delete()
