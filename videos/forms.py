from django import forms

from videos.models import Video


class VideoForm(forms.ModelForm):
    post = forms.CharField(
              label="",
              widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter video title here'}),  # noqa: E501
              max_length=255
                           )

    class Meta:
        model = Video
        fields = ['post', 'video_file']

    def clean_video_file(self):

        VIDEO_FILE_TYPES = ['mp4']

        uploaded_video = self.cleaned_data.get("video_file",  False)

        extension = str(uploaded_video).split('.')[-1]

        file_type = extension.lower()

        if not uploaded_video:
            raise forms.ValidationError("please upload a video")

        if file_type not in VIDEO_FILE_TYPES:
            raise forms.ValidationError("Upload an mp4 file")

        return uploaded_video
