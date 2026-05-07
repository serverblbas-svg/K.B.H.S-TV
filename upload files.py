<!-- بەشی ئەپڵۆدکردنی ڕاستەقینە -->
<section class="card" style="margin-top: 30px;">
    <h2><i class="fas fa-upload"></i> بارکردنی فایل بۆ Spi TV</h2>
    <div style="background: white; padding: 20px; border-radius: 10px; border: 2px dashed #2c5e2e; text-align: center;">
        <input type="file" id="fileSelector" style="margin-bottom: 10px; display: block; width: 100%;">
        <progress value="0" max="100" id="uploadProgress" style="width: 100%; height: 20px; display: none;"></progress>
        <p id="uploadStatus" style="font-size: 14px; margin-top: 10px;"></p>
        <button onclick="uploadToFirebase()" style="background: #2c5e2e; color: white; border: none; padding: 10px 25px; border-radius: 5px; cursor: pointer;">بارکردن (Upload)</button>
    </div>
</section>

<!-- پێویستە ئەم دوو سکریپتە زیاد بکەیت پێش کۆتایی body -->
<script src="https://www.gstatic.com/firebasejs/8.10.0/firebase-app.js"></script>
<script src="https://www.gstatic.com/firebasejs/8.10.0/firebase-storage.js"></script>

<script>
    // --- لێرەدا دەبێت کۆنفیگی فایەربەیسی خۆت دابنێیت ---
    const firebaseConfig = {
        apiKey: "YOUR_API_KEY",
        authDomain: "your-app.firebaseapp.com",
        projectId: "your-app-id",
        storageBucket: "your-app.appspot.com",
        messagingSenderId: "your-id",
        appId: "your-app-id"
    };

    // ئینیشیالایز کردنی فایەربەیس
    firebase.initializeApp(firebaseConfig);
    const storage = firebase.storage();

    function uploadToFirebase() {
        const file = document.getElementById('fileSelector').files[0];
        if (!file) {
            alert("تکایە سەرەتا فایلێک هەڵبژێرە!");
            return;
        }

        const storageRef = storage.ref('spi_uploads/' + file.name);
        const uploadTask = storageRef.put(file);
        const progressTag = document.getElementById('uploadProgress');
        const statusTag = document.getElementById('uploadStatus');

        progressTag.style.display = 'block';

        uploadTask.on('state_changed', 
            (snapshot) => {
                let progress = (snapshot.bytesTransferred / snapshot.totalBytes) * 100;
                progressTag.value = progress;
                statusTag.innerText = "خەریکی بارکردنە: " + Math.round(progress) + "%";
            }, 
            (error) => {
                alert("هەڵەیەک ڕوویدا: " + error.message);
            }, 
            () => {
                uploadTask.snapshot.ref.getDownloadURL().then((downloadURL) => {
                    statusTag.innerHTML = `✅ بە سەرکەوتوویی بارکرا! <br> <a href="${downloadURL}" target="_blank">لینکی فایلەکە لێرەیە</a>`;
                    console.log('File available at', downloadURL);
                });
            }
        );
    }
</script>
