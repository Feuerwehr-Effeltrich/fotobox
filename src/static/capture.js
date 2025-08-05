const START_VALUE = 5;

class FotoboxController {
    constructor() {
        this.countdown = START_VALUE;
        this.isRunning = false;
        this.countdownInterval = null;

        this.overlayCountdown = document.getElementById('overlayCountdown');
        this.countdownOverlay = document.getElementById('countdownOverlay');
        this.captureButton = document.getElementById('captureButton');

        this.initializeEventListeners();
    }

    initializeEventListeners() {
        this.captureButton.addEventListener('click', () => {
            if (!this.isRunning) {
                this.startCountdown();
            }
        });
    }

    updateOverlayCountdown() {
        this.overlayCountdown.textContent = this.countdown;
    }

    startCountdown() {
        this.isRunning = true;
        this.captureButton.disabled = true;

        // Show the overlay and start with the initial countdown value
        this.countdownOverlay.classList.add('active');
        this.updateOverlayCountdown();

        this.countdownInterval = setInterval(() => {
            this.countdown--;
            this.updateOverlayCountdown();

            if (this.countdown <= 0) {
                this.stopCountdown();
                this.capturePhoto();
            }
        }, 1000);
    }

    stopCountdown() {
        if (this.countdownInterval) {
            clearInterval(this.countdownInterval);
            this.countdownInterval = null;
        }

        this.isRunning = false;
        this.captureButton.disabled = false;

        // Hide the overlay
        this.countdownOverlay.classList.remove('active');

        this.countdown = START_VALUE;
    }

    async capturePhoto() {
        try {
            const response = await fetch('/capture', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    timestamp: new Date().toISOString()
                })
            });

            if (response.ok) {
                this.showCaptureFeedback();
            }
        } catch (error) {
            console.error('Error capturing photo:', error);
        }
    }

    showCaptureFeedback() {
        // add a visual flash effect to indicate photo was taken
        const flash = document.createElement('div');
        flash.className = 'flash';

        document.body.appendChild(flash);

        // fade out
        setTimeout(() => {
            flash.style.opacity = '0';
            setTimeout(() => {
                document.body.removeChild(flash);
            }, 300);
        }, 100);
    }
}

// Initialize the fotobox controller when the page loads
document.addEventListener('DOMContentLoaded', () => {
    new FotoboxController();
});
