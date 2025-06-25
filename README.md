
````markdown
# 🚗 Vehicle Control Simulation & Test Automation

A Python-based simulation and testing framework for validating vehicle control algorithms like MPC, PID, and iLQR.  
This project is based on the [HybridRobotics/car-racing](https://github.com/HybridRobotics/car-racing) repository and demonstrates structured test automation, simulation control, and CI/CD integration.

---

## 📌 Features

- ✅ Simulation of vehicle dynamics and racing environments  
- ✅ Control algorithms: MPC, PID, iLQR  
- ✅ Automated testing using PyTest  
- ✅ Uses CasADi and CVXOPT for control modeling and optimization  
- ✅ CI-ready with GitHub Actions  
- ✅ Visual output with plotting and animations

---

## ⚙️ Technologies Used

- **Language**: Python  
- **Libraries**: CasADi, CVXOPT, Matplotlib, NumPy, PyTest  
- **Dev Tools**: Git, GitHub Actions, Conda, VS Code

---

## 🛠️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/vehicle-control-simulation.git
cd vehicle-control-simulation
````

### 2. Create Conda environment

```bash
conda env create -f environment.yml
conda activate car-racing
pip install -e .
```

### 3. Run All Tests

```bash
pytest
```

### 4. Run a Specific Test (e.g., controller)

```bash
python car_racing/tests/control_test.py \
  --ctrl-policy mpc-lti \
  --track-layout l_shape \
  --simulation \
  --plotting \
  --animation
```

---

## 📁 Project Structure

```
car-racing/
├── car_racing/
│   ├── control/             # Control algorithms (MPC, iLQR, etc.)
│   ├── racing/              # Simulation logic
│   ├── utils/               # Utility modules
├── tests/                   # Test scripts using PyTest
├── environment.yml          # Conda environment dependencies
├── README.md
```

---

## 📸 Screenshots

*(Add GIFs or images of the animation and plots here)*

---

## 📄 License

This project is built for educational and research purposes based on HybridRobotics/car-racing (MIT License).

---

## 🙋‍♂️ Author

**Vynkatesh Sinhasane**
🔗 [LinkedIn](https://linkedin.com/in/vynkatesh-sinhasane) | 📧 [vynkateshsinhasane95@gmail.com](mailto:vynkateshsinhasane95@gmail.com
