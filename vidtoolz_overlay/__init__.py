import vidtoolz

from moviepy import CompositeVideoClip, VideoFileClip, vfx


def overlay_video(
    background_path,
    overlay_path,
    output_path,
    overlay_start=0,
    overlay_end=None,
    position_time=0,
    fade_duration=0.5,
):
    # Load background video
    background = VideoFileClip(background_path)

    # Load overlay video and remove audio
    overlay = VideoFileClip(overlay_path).without_audio()

    # Subclip overlay
    if overlay_end is not None:
        overlay = overlay.subclipped(overlay_start, overlay_end)
    else:
        overlay = overlay.subclipped(overlay_start)

    # Resize overlay to match background
    overlay = overlay.resized(background.size)

    # Apply fade in and fade out

    overlay = overlay.with_effects(
        [vfx.CrossFadeIn(fade_duration), vfx.CrossFadeOut(fade_duration)]
    )

    # Set overlay start time
    overlay = overlay.with_start(position_time)

    # Composite final video
    final = CompositeVideoClip([background, overlay])

    # Match background duration
    final = final.with_duration(background.duration)

    # Write output
    final.write_videofile(output_path, codec="libx264", audio_codec="aac")


# # Example usage
# overlay_video(
#     background_path="background.mp4",
#     overlay_path="overlay.mp4",
#     output_path="output.mp4",
#     overlay_start=5,
#     overlay_end=10,
#     position_time=2,
#     fade_duration=0.5,
# )


def create_parser(subparser):
    parser = subparser.add_parser(
        "overlay", description="Add overlay video on a video using moviepy"
    )
    # Add subprser arguments here.
    parser.add_argument("-test", "--test", type=str, help="Example argument")
    return parser


class ViztoolzPlugin:
    """Add overlay video on a video using moviepy"""

    __name__ = "overlay"

    @vidtoolz.hookimpl
    def register_commands(self, subparser):
        self.parser = create_parser(subparser)
        self.parser.set_defaults(func=self.run)

    def run(self, args):
        # add actual call here
        pass

    def hello(self, args):
        # this routine will be called when "vidtoolz "overlay is called."
        print("Hello! This is an example ``vidtoolz`` plugin.")


overlay_plugin = ViztoolzPlugin()
