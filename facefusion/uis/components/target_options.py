import os
import shutil
from typing import Optional, Tuple
import gradio
import yt_dlp

from facefusion import wording
from facefusion.uis.core import get_ui_component
from facefusion.filesystem import get_temp_directory_path, is_directory, create_temp

TARGET_URL_TEXTBOX : Optional[gradio.Textbox] = None
DOWNLOAD_BUTTON : Optional[gradio.Button] = None


def render() -> None:
	global TARGET_URL_TEXTBOX
	global DOWNLOAD_BUTTON

	TARGET_URL_TEXTBOX = gradio.Textbox(
		label = wording.get('uis.target_url_textbox_label'),
		max_lines = 1
	)
	DOWNLOAD_BUTTON = gradio.Button(
		value = wording.get('uis.download_button_label'),
		size = 'sm'
	)


def listen() -> None:
	target_file = get_ui_component('target_file')
	preview_frame_slider = get_ui_component('preview_frame_slider')
	if target_file and preview_frame_slider:
		DOWNLOAD_BUTTON.click(download, inputs = TARGET_URL_TEXTBOX, outputs = [ target_file, preview_frame_slider ])


def download(target_url : str) -> Tuple[gradio.File, gradio.Slider]:
	temp_directory_path = get_temp_directory_path('target_download.mp4')
	temp_file_path = os.path.join(temp_directory_path, 'target_download.mp4')
	if is_directory(temp_directory_path):
		shutil.rmtree(temp_directory_path)
	create_temp('target_download.mp4')

	youtube_download_options =\
	{
		'outtmpl': temp_file_path,
		'format': 'mp4'
	}
	if target_url:
		try:
			with yt_dlp.YoutubeDL(youtube_download_options) as youtube_download:
				youtube_download.download(target_url)
			return gradio.File(value = temp_file_path), gradio.Slider(value = 0)
		except yt_dlp.utils.DownloadError:
			pass
	return gradio.File(value = None), gradio.Slider(value = 0)
