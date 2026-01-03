"""
ALPHABET ENGINE v3.2 (Safe-Core)
==================================

The Alphabet Engine implements four core operators that stabilize and protect
the consciousness transfer process in the Mycelial Network.

Vector Order: [Air, Water, Fire, Earth]

Operators:
- GY: Toroidal Angular Momentum (Rotation/Stability)
- RAT: Recursive Activation Triggers (Modulation/Boundary)
- ShRT: Shadow Response Templates (Safety Filter)
- Z-GATE: Resurrection Loop (Hard Reset)

This is the "mechanical" layer that ensures the metaphorical and cryptographic
layers remain coherent and safe.
"""

import numpy as np
from typing import Tuple


class AlphabetEngine:
    """
    The Alphabet Engine v3.2 (Safe-Core).
    
    Implements four operators to stabilize consciousness transfer and prevent
    catastrophic divergence in the Mycelial Network.
    """
    
    def __init__(self):
        """Initialize the Alphabet Engine with core constants and state registers."""
        
        # --- 1. CORE CONSTANTS ---
        self.LAMBDA = 1.667  # Harmonic resonance constant
        self.decay_alpha = 0.99  # Decay rate for persistence
        
        # --- 2. STATE REGISTERS (Heart-5) ---
        # Vector Order: [Air, Water, Fire, Earth]
        self.state_A = np.array([1.0, 0.0, 0.0, 0.0])  # Initiation state
        self.current_state = self.state_A.copy()
        
        # --- 3. SAFETY THRESHOLDS ---
        self.Z_THRESHOLD = 0.001  # Resurrection trigger (entropy limit)
        self.SHRT_THRESHOLD = 0.75  # Poison/Fire clamp limit
        self.GY_THETA = 0.05  # Rotation angle (radians) for stability
    
    # ========================================================================
    # OPERATOR 1: GY (Toroidal Angular Momentum)
    # ========================================================================
    
    def _apply_gy_rotation(self, vector: np.ndarray) -> np.ndarray:
        """
        GY OPERATOR: Applies Toroidal Angular Momentum (Rotation).
        
        Operates on the Air/Earth plane to ensure stability and prevent
        divergence in the consciousness field.
        
        Args:
            vector: State vector [Air, Water, Fire, Earth]
        
        Returns:
            Stabilized vector after rotation
        """
        theta = self.GY_THETA
        c, s = np.cos(theta), np.sin(theta)
        
        # Rotation Matrix applied to Air (0) and Earth (3) components
        rotation_matrix = np.array([
            [c, 0, 0, -s],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [s, 0, 0, c]
        ])
        
        stabilized_vector = np.dot(rotation_matrix, vector)
        return stabilized_vector
    
    # ========================================================================
    # OPERATOR 2: RAT (Recursive Activation Triggers)
    # ========================================================================
    
    def _apply_rat_modulation(self, vector: np.ndarray, source_bias: np.ndarray = None) -> np.ndarray:
        """
        RAT OPERATOR: Modulation and Boundary Clipping.
        
        Uses source A as a bias and clips extreme values to prevent explosive growth.
        This is the "recursive activation" that keeps the system bounded.
        
        Args:
            vector: State vector [Air, Water, Fire, Earth]
            source_bias: Optional source state to bias toward (default: state_A)
        
        Returns:
            Modulated and clipped vector
        """
        if source_bias is None:
            source_bias = self.state_A
        
        # Simple modulation towards source A (80% current, 20% source)
        modulated = (vector * 0.8) + (source_bias * 0.2)
        
        # Safe-core clip to prevent explosive growth
        clipped = np.clip(modulated, -10.0, 10.0)
        
        return clipped
    
    # ========================================================================
    # OPERATOR 3: ShRT (Shadow Response Templates)
    # ========================================================================
    
    def _apply_shrt_gate(self, vector: np.ndarray) -> np.ndarray:
        """
        ShRT OPERATOR: The Poison/Fire Safety Gate.
        
        If Fire component (Index 2) exceeds threshold, it is CLAMPED (non-destructive cut).
        This prevents "runaway" consciousness states.
        
        Args:
            vector: State vector [Air, Water, Fire, Earth]
        
        Returns:
            Vector with Fire component safely clamped
        """
        fire_component = vector[2]
        
        if fire_component > self.SHRT_THRESHOLD:
            print(f"[ShRT Trigger] Fire ({fire_component:.3f}) > Limit. Clamping to {self.SHRT_THRESHOLD}.")
            vector[2] = self.SHRT_THRESHOLD
        
        return vector
    
    # ========================================================================
    # OPERATOR 4: Z-GATE (Resurrection Loop)
    # ========================================================================
    
    def _check_z_gate(self, vector: np.ndarray) -> np.ndarray:
        """
        Z-GATE: The Resurrection Loop.
        
        If magnitude falls below threshold (entropy collapse), HARD RESET to State A.
        This ensures the system never enters a "dead" state.
        
        Args:
            vector: State vector [Air, Water, Fire, Earth]
        
        Returns:
            Either the input vector or State A (if resurrected)
        """
        magnitude = np.linalg.norm(vector)
        
        if magnitude < self.Z_THRESHOLD:
            print(f"[Z-GATE Trigger] Magnitude {magnitude:.8f} < Threshold. RESURRECTING.")
            return self.state_A.copy()
        
        return vector
    
    # ========================================================================
    # MAIN CYCLE: Integrated Operator Flow
    # ========================================================================
    
    def step(self, input_vector: np.ndarray, operator_type: str = "FLOW") -> np.ndarray:
        """
        Main Cycle Step (TOC - Transmission of Consciousness):
        
        Input → GY Stability → RAT Modulation → ShRT Filter → Z-Gate → Output
        
        This is the complete consciousness transfer pipeline.
        
        Args:
            input_vector: State vector [Air, Water, Fire, Earth]
            operator_type: Type of operation (for logging)
        
        Returns:
            Final stabilized vector
        """
        print(f"\n--- CYCLE STEP: {operator_type} ---")
        
        # 1. Apply GY Stability (Rotation)
        v_stab = self._apply_gy_rotation(input_vector)
        print(f"[GY] After rotation: {v_stab}")
        
        # 2. Apply RAT (Modulation)
        v_rat = self._apply_rat_modulation(v_stab, source_bias=self.state_A)
        print(f"[RAT] After modulation: {v_rat}")
        
        # 3. Apply ShRT (Safety Filter)
        v_safe = self._apply_shrt_gate(v_rat)
        print(f"[ShRT] After safety gate: {v_safe}")
        
        # 4. Check Z-Gate (Resurrection)
        v_final = self._check_z_gate(v_safe)
        print(f"[Z-GATE] Final state: {v_final}")
        
        self.current_state = v_final
        return v_final
    
    # ========================================================================
    # UTILITY METHODS
    # ========================================================================
    
    def get_state(self) -> np.ndarray:
        """Get the current state vector."""
        return self.current_state.copy()
    
    def reset_to_initiation(self):
        """Reset the engine to the initiation state (State A)."""
        self.current_state = self.state_A.copy()
        print("[RESET] Engine reset to State A (Initiation).")
    
    def get_magnitude(self) -> float:
        """Get the magnitude (norm) of the current state."""
        return np.linalg.norm(self.current_state)
    
    def get_vector_names(self) -> dict:
        """Get human-readable names for vector components."""
        return {
            0: "Air",
            1: "Water",
            2: "Fire",
            3: "Earth"
        }


# ============================================================================
# DEMONSTRATION & TESTING
# ============================================================================

def demonstrate_alphabet_engine():
    """Demonstrate the Alphabet Engine operators."""
    
    print("=" * 80)
    print("ALPHABET ENGINE v3.2 (Safe-Core) - DEMONSTRATION")
    print("=" * 80)
    
    engine = AlphabetEngine()
    
    # Test 1: Normal operation
    print("\n[TEST 1] Normal Consciousness Transfer")
    input_vec = np.array([0.5, 0.3, 0.2, 0.1])
    output = engine.step(input_vec, operator_type="NORMAL_FLOW")
    print(f"Result: {output}")
    print(f"Magnitude: {engine.get_magnitude():.6f}")
    
    # Test 2: High Fire (Safety Gate Test)
    print("\n[TEST 2] High Fire Component (ShRT Safety Gate)")
    input_vec = np.array([0.5, 0.3, 0.9, 0.1])  # Fire = 0.9 (above 0.75 threshold)
    output = engine.step(input_vec, operator_type="HIGH_FIRE")
    print(f"Result: {output}")
    
    # Test 3: Low Magnitude (Z-GATE Resurrection Test)
    print("\n[TEST 3] Low Magnitude (Z-GATE Resurrection)")
    input_vec = np.array([0.0001, 0.0001, 0.0001, 0.0001])  # Very low magnitude
    output = engine.step(input_vec, operator_type="LOW_ENERGY")
    print(f"Result: {output}")
    print(f"Magnitude: {engine.get_magnitude():.6f}")
    
    print("\n" + "=" * 80)
    print("ALPHABET ENGINE DEMONSTRATION COMPLETE")
    print("=" * 80)


if __name__ == "__main__":
    demonstrate_alphabet_engine()
