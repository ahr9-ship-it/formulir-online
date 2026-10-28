const SHEET_ID = "https://docs.google.com/spreadsheets/d/1zSe2_2rkbQ-2WVBH74kJDZLJPWLjhNmdl9w3tbSMmU4/edit?gid=0#gid=0";
const SHEET_NAME = "Jawaban"

function doPost(e) {
    try {
      const data = JSON.parse(e.postData.contents);

      const sheet = SpreadsheetApp
          .openById(SHEET_ID)
          .getSheetByName(SHEET_NAME);
      
      if (!sheet){
        throw new Error("Sheet Jawaban Tidak Ditemukan.")
      }

      if (sheet.getLastRow() === 0) {
        sheet.appendRow([
          "Waktu",
          "Nama",
          "First",
          "Now",
          "Message",
          "Memory",
          "Advice",
          "secret"
        ]);
      }

      sheet.appendRow([
        new Date (),
        data.nama || "Anonim",
        data.first || "",
        data.now || "",
        data.message || "",
        data.memory || "",
        data.advive || "",
        data.secret || ""
      ]);

      return ContentService
        .createTextOutput(JSON.stringify({successs: true}))
        .setMimeType(ContentSevice.MimeType.JSON);
    
    } catch (error){
      return ContentService
        .createTextOutput(JSON,stringify({
          succes: false,
          error: error.message
        }))
        . setMimeType(ContentService.MimeType,JSON); }
        }
