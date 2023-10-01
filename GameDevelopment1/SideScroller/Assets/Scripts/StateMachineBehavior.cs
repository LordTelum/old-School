using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Events;

public class StateMachineBehaviour : MonoBehaviour
{
    private Animator animator;
    // Start is called before the first frame update
    private void Start()
    {
        animator = GetComponent<Animator>();
    
    }
    public void IsWalking()
    {
        animator.SetTrigger("WalkTrigger");
    }

    public void IsJumping()
    {
        animator.SetTrigger("JumpTrigger");
    }

    public void Die()
    {
        animator.SetTrigger("DieTrigger");
    }
}
