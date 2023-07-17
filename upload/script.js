const MAX_PDF_SIZE = 1000000

      /* ENTER YOUR ENDPOINT HERE */

      const API_ENDPOINT = 'https://ottyf0g6dg.execute-api.eu-central-1.amazonaws.com/uploads'

      new Vue({
        el: '#app',
        data: {
          pdf: null,
          uploadURL: '',
          result: '',
        },
        methods: {
          onFileChange(e) {
            let files = e.target.files || e.dataTransfer.files
            if (!files.length) return
            this.createPDF(files[0])
          },
          createPDF(file) {
            if (file.type !== 'application/pdf') {
              return alert('Wrong file type - PDF only.')
            }
            if (file.size > MAX_PDF_SIZE) {
              return alert('PDF is too large.')
            }
            this.pdf = file
          },
          removePDF() {
            this.pdf = null
          },
          async uploadPDF() {
            console.log('Upload clicked')
            // Get the presigned URL
            try {
              const response = await axios.get(API_ENDPOINT)
              console.log('Response: ', response.data)

              console.log('Uploading: ', this.pdf)
              const result = await axios.put(response.data.uploadURL, this.pdf, {
                headers: {
                  'Content-Type': 'application/pdf',
                },
              })
              console.log('Result: ', result)

              // Final URL for the user doesn't need the query string params
              this.uploadURL = response.data.uploadURL.split('?')[0]
            } catch (error) {
              console.error(error)
              alert('Error uploading PDF.')
            }
          },
          async checkResult() {
            try {
              const response = await axios.get(
                'https://ctzl7xdyo74vmi2a2oqv36dj240ltrkg.lambda-url.eu-central-1.on.aws/'
              )
              console.log('Result:', response.data)
              this.result = response.data
            } catch (error) {
              console.error(error)
              alert('Błąd podczas sprawdzania wyniku.')
            }
          },
          refreshPage() {
            location.reload();
        }}
      })