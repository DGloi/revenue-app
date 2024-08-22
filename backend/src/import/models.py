from django.db import models

# Create your models here.

class ImportFileList(models.Model):
    provider = models.CharField(max_length=255)
    file_name = models.CharField(max_length=255)
    isEmpty = models.BooleanField(default=False)
    countRecords = models.IntegerField(default)
    uploaded_at = models.DateTimeField(auto_now_add=True)

class AdyenPaymentAccountingReport(models.Model):
    file = models.FileField(upload_to='uploads/')
    merchantAccount = models.CharField(max_length=255)
    pspReference = models.CharField(max_length=255)
    merchantReference = models.CharField(max_length=255)
    paymentMethod = models.CharField(max_length=255)
    bookingDate = models.timestamp()
    timeZone = models.CharField(max_length=10)
    mainAmount = models.DecimalField(max_digits=5)
    mainCurrency = models.CharField(max_length=3)
    recordType = models.CharField(max_length=255)
    paymentCurrency = models.CharField(max_length=3)
    receivedPC = models.DecimalField(max_digits=5)
    authorisedPC = models.DecimalField(max_digits=5)
    capturedPC = models.DecimalField(max_digits=5)
    settlementCurrency = models.CharField(max_length=3)
    payableSC = models.DecimalField(max_digits=5)
    commission = models.DecimalField(max_digits=5)
    markupSC = models.DecimalField(max_digits=5)
    schemeFeesSC = models.DecimalField(max_digits=5) 
    interchangeSC = models.DecimalField(max_digits=5)
    processingFeeCurrency = models.CharField(max_length=3)
    processingFeeFC = models.DecimalField(max_digits=5)
    userName = models.CharField(max_length=255)
    paymentMethodVariant = models.CharField(max_length=255)
    issuerCountry = models.CharField(max_length=2)
    shopperCountry = models.CharField(max_length=2)
    modificationMerchantReference = models.CharField(max_length=255)
    payableBatch = models.CharField(max_length=255)
    uniqueTerminalID = models.CharField(max_length=255)
    bookingDateAMS = models.timestamp()
    creationDate = models.timestamp()
    creationDateAMS = models.timestamp()
    payoutDate = models.timestamp()
    gratuityAmount = models.DecimalField(max_digits=5)
    icsfDetails = models.CharField(max_length=255) 
    cardNumber = models.CharField(max_length=255)
    acquirer = models.CharField(max_length=255)
    acquirerAccount = models.CharField(max_length=255)
    mid = models.CharField(max_length=255)
    acquirerAuthCode = models.CharField(max_length=255) 
    acquirerReference = models.CharField(max_length=255)
    arn = models.CharField(max_length=255)
    originalAmount = models.DecimalField(max_digits=5)
    installmentsPC = models.DecimalField(max_digits=5)
    advancedPC = models.DecimalField(max_digits=5)
    advancementCode = models.CharField(max_length=255)
    advancementBatch = models.CharField(max_length=255)
    bookingType = models.CharField(max_length=255)
    advancementFeePercentage = models.DecimalField(max_digits=5) 
    installments = models.IntegerField()
    metadata = models.CharField(max_length=255)
    merchantOrderReference = models.CharField(max_length=255)
    store = models.CharField(max_length=255)
    issuerName = models.CharField(max_length=255)
    riskPremium = models.BooleanField()
    registerBookingType = models.CharField(max_length=255)
    modificationPspReference = models.CharField(max_length=255)
    shopperReference = models.CharField(max_length=255)
    shopperName = models.CharField(max_length=255)
    paymentAccountReference = models.CharField(max_length=255)
    tenderreference = models.CharField(max_length=255)
    dccMarkupSC = models.DecimalField(max_digits=5)
    globalCardBrand = models.CharField(max_length=255)
    
    def __str__(self):
        return self.file.name
