import "htmx.org";
import Alpine from "alpinejs";

document.addEventListener("alpine:init", () => {
  Alpine.data("uploadMedia", () => ({
    images: [],
    videos: [],
    uploadImage(evt) {
      const file = evt.target.files[0];
      const formData = new FormData();
      formData.append("image", file);

      fetch("/posts/image/upload/", {
        method: "POST",
        body: formData,
        headers: {
          "X-CSRFToken": document.querySelector("input[name=csrfmiddlewaretoken]").value
        }
      })
        .then(response => response.json())
        .then(data => {
          if (data.url) {
            this.images.push({ name: file.name, url: data.url });
          } else {
            alert("Image upload failed");
          }
        })
        .catch(error => {
          console.error("Error", error);
        });
    },
    uploadVideo(evt) {
      const file = evt.target.files[0];
      const formData = new FormData();
      formData.append("video", file);

      fetch("/posts/video/upload/", {
        method: "POST",
        body: formData,
        headers: {
          "X-CSRFToken": document.querySelector("input[name=csrfmiddlewaretoken]").value
        }
      })
        .then(response => response.json())
        .then(data => {
          if (data.url) {
            this.videos.push({ name: file.name, url: data.url });
          } else {
            alert("Video upload failed");
          }
        })
        .catch(error => {
          console.log("Error", error);
        })
    }
  }));
});

Alpine.start();
