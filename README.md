Text-to-Speech Cloud Function
===


**Author:** Deniss Tsokarev

**License:** *see [LICENSE.TXT](https://github.com/dents0/text-to-speech-cf/blob/master/LICENSE.txt)*


Description
---
A Cloud Function triggered by the Cloud Storage *"finalize/create"* event.

When a **txt** file is uploaded or updated in a specified bucket, 
an **mp3** file with the same name will be generated.


Prerequisites
---
* [Google Cloud Platform](https://console.cloud.google.com/) project with [billing](https://cloud.google.com/billing/docs/how-to/modify-project) enabled.
* Enabled [Cloud Functions API](https://console.cloud.google.com/apis/library/cloudfunctions.googleapis.com)
* Enabled [Cloud Text-to-Speech API](https://console.cloud.google.com/apis/library/texttospeech.googleapis.com)


How to use
---
1. Create a [**GCS bucket**](https://cloud.google.com/storage/docs/creating-buckets) in which you will generate the mp3 files.
2. Create a [**Cloud Function**](https://cloud.google.com/functions/docs/deploying/console) selecting *Cloud Storage* as its trigger.
3. For the **Event Type** choose *Finalize/Create* event.
4. Select the **bucket** you have created during Step 1.
5. **Deploy** the Cloud Function.

